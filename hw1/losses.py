"""Loss functions for imitation learning.

Each loss function takes the model/policy, a batch of states, and a batch of
expert actions, and returns a scalar loss. This signature keeps the training
loop in main.py generic across all methods.

Structure:
    TODO (students implement):
        - mse_loss (Problem 1): MSE regression loss for behavior cloning.
        - flow_matching_loss (Problem 3): MSE loss between predicted and
          target velocity. Compare with diffusion_loss for the pattern.
"""

import torch
import torch.nn as nn


def mse_loss(policy, s_batch: torch.Tensor,
             a_batch: torch.Tensor) -> torch.Tensor:
    """Compute the MSE regression loss for behavior cloning.

    Args:
        policy: BCPolicy network (callable: s_batch -> predicted actions).
        s_batch: states, shape (B, state_dim).
        a_batch: expert actions, shape (B, action_dim).

    Returns:
        Scalar MSE loss (mean over batch and action dimensions).
    """
    # ============================================================
    # TODO: Implement mse_loss.
    # ============================================================
    pred_a = policy(s_batch)
    loss = nn.functional.mse_loss(pred_a, a_batch)
    return loss


def flow_matching_loss(policy, s_batch: torch.Tensor,
                       a_batch: torch.Tensor) -> torch.Tensor:
    """Compute the flow matching loss (MSE on velocity prediction).

    The policy (FlowMatchingPolicy) carries its own schedule.

    Args:
        policy: FlowMatchingPolicy (model + schedule).
        s_batch: states, shape (B, state_dim).
        a_batch: expert actions, shape (B, action_dim).

    Returns:
        Scalar MSE loss (mean over batch and action dimensions).
    """
    # ============================================================
    # TODO: Implement flow matching loss.
    # ============================================================
    t = torch.rand(a_batch.shape[0], device=a_batch.device)  # uniform dist
    noisy_a_t, velocity = policy.schedule.interpolate(a_batch, t)
    pred_velocity = policy(noisy_a_t, s_batch, t)
    loss = nn.functional.mse_loss(pred_velocity, velocity)
    return loss
