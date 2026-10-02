# Homework 3
* Brief [instructions] for [Homework3].
* For detailed executions, see [run_hw3.ipynb] and [run_hw3_modal.ipynb].

## Note
* Implemented algorithms:
  * [x] Advantage Weighted Actor Critic (AWAC)
  * [x] Implicit Q-Learning (IQL)
* Adjusted camera angles during evaluation rendering for a clearer view.

## Result
### AntMaze - UMaze
* Learning curves  
  (x-axis: timesteps)  
  <img src="results/colab_antmaze_umaze.png" width="49%" /> <img src="results/modal_antmaze_umaze.png" width="49%" />
* Evaluation rollouts
  * AWAC  
    <img src="modal_results/hw3_awac_antmaze_umaze_seed1/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_awac_antmaze_umaze_seed2/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_awac_antmaze_umaze_seed3/eval_traj_last.gif" width="32.5%" />
  * IQL, `zeta = 0.2`  
    <img src="modal_results/hw3_iql_zeta_0.2_umaze_seed1/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.2_umaze_seed2/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.2_umaze_seed3/eval_traj_last.gif" width="32.5%" />
  * IQL, `zeta = 0.9`  
    <img src="modal_results/hw3_iql_zeta_0.9_umaze_seed1/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_umaze_seed2/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_umaze_seed3/eval_traj_last.gif" width="32.5%" />

### AntMaze - Medium-Diverse
* Learning curves  
  <img src="results/colab_antmaze_medium.png" width="49%" /> <img src="results/modal_antmaze_medium.png" width="49%" />
* Evaluation rollouts
  * AWAC  
    <img src="modal_results/hw3_awac_antmaze_medium_diverse_seed1/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_awac_antmaze_medium_diverse_seed2/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_awac_antmaze_medium_diverse_seed3/eval_traj_last.gif" width="32.5%" />
    Note that the ant in the third evaluation video actually fails—it doesn't reach the goal at the top-right corner.
  * IQL, `zeta = 0.9`  
    <img src="modal_results/hw3_iql_zeta_0.9_medium_diverse_seed1/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_medium_diverse_seed2/eval_traj_last.gif" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_medium_diverse_seed3/eval_traj_last.gif" width="32.5%" />

### PointMass - Medium
* Learning curves  
  <img src="results/colab_pointmass_medium.png" width="49%" /> <img src="results/modal_pointmass_medium.png" width="49%" />
* Evaluation rollouts
  * Filtered BC  
    <img src="modal_results/hw3_filtered_bc_stitching_seed1/eval_last_traj.png" width="32.5%" /> <img src="modal_results/hw3_filtered_bc_stitching_seed2/eval_last_traj.png" width="32.5%" /> <img src="modal_results/hw3_filtered_bc_stitching_seed3/eval_last_traj.png" width="32.5%" />
  * IQL, `zeta = 0.9`  
    <img src="modal_results/hw3_iql_zeta_0.9_stitching_seed1/eval_last_traj.png" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_stitching_seed2/eval_last_traj.png" width="32.5%" /> <img src="modal_results/hw3_iql_zeta_0.9_stitching_seed3/eval_last_traj.png" width="32.5%" />



[instructions]: README_.md
[Homework3]: https://cs224r.stanford.edu/material/hw3/CS224R_2026_Homework_3.pdf
[run_hw3.ipynb]: run_hw3.ipynb
[run_hw3_modal.ipynb]: run_hw3_modal.ipynb
