# Joint-Motion Interactive Learning for Human Pose Estimation in Video

## Abstract
Human pose estimation in video has long been an ongoing compelling yet challenging problem with significant implications in practice. Most existing approaches aim to refine and incorporate temporal clues (heatmaps \textit{or} features) from the consecutive frames to estimate the human pose in the keyframe. One aspect that has been overlooked is that when pose estimation is confronted with video defocus, 1) relying solely on frame features may lead to the neglect of certain joints, and 2) relying exclusively on heatmaps may disregard the semantic relationships between joints, potentially resulting in performance deterioration. 
	
To tackle this issue, we propose a novel joint-motion interactive learning framework for pose estimation that effectively focuses on regional joint (heatmap) cues and overall motion features. Specifically, we introduce a context-aware joint learner that is guided by heatmaps to extract context-aware features of joint regions from motion features of consecutive frames. Joint features supply context-aware information about joint regions, while motion features could provide semantic relationships between joints. Considering their strengths, we further propose a joint-motion interactive learning that mutually amalgamates the complementary representations between joint and motion features. More importantly, to grasp more diverse joint and motion features, we theoretically analyze and propose a mutual information objective between them. Empirical experiments demonstrate that our method outperforms prior arts on three challenging benchmarks. Our code is released available at https://github.com/IJCAI2024-1731/JMI-Pose, hoping that it will be useful to the community.

## Method Overview

![image](https://github.com/IJCAI2024-1731/JMI-Pose/blob/main/figs/fig22.jpg)

## Visualization comparison
![image](https://github.com/IJCAI2024-1731/JMI-Pose/blob/main/figs/fig44.jpg)

## More visual results
![image](https://github.com/IJCAI2024-1731/JMI-Pose/blob/main/figs/fig5.jpg)
