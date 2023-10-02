import argparse

import numpy as np
import PIL
from tqdm import tqdm

from track_anything.tools.interact_tools import SamControler
from track_anything.xmem.base_tracker import BaseTracker


class TrackingAnything:
    def __init__(self, sam_checkpoint, xmem_checkpoint, sam_model_type="vit_h", device="cuda:0"):
        self.sam_checkpoint = sam_checkpoint
        self.xmem_checkpoint = xmem_checkpoint
        self.samcontroler = SamControler(self.sam_checkpoint, sam_model_type, device)
        self.xmem = BaseTracker(self.xmem_checkpoint, device=device)

    def first_frame_click(self, image: np.ndarray, points: np.ndarray, labels: np.ndarray, multimask=True):
        mask, logit, painted_image = self.samcontroler.first_frame_click(image, points, labels, multimask)
        return mask, logit, painted_image

    def generator(self, images: list, template_mask: np.ndarray):
        masks = []
        logits = []
        painted_images = []
        for i in tqdm(range(len(images)), desc="Tracking image"):
            if i == 0:
                mask, logit, painted_image = self.xmem.track(images[i], template_mask)
                masks.append(mask)
                logits.append(logit)
                painted_images.append(painted_image)

            else:
                mask, logit, painted_image = self.xmem.track(images[i])
                masks.append(mask)
                logits.append(logit)
                painted_images.append(painted_image)
        return masks, logits, painted_images
