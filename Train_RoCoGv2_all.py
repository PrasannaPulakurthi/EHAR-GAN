import mmengine
import mmaction
from mmengine.runner import Runner
from mmengine.runner import set_random_seed
from mmengine import Config
import os.path as osp
import os
import torch

def find_best_model_checkpoint(checkpoints_dir, best_model_prefix='best_'):
    """
    Search for the best model checkpoint in the given directory based on a prefix.
    """
    best_model_filename = None
    for filename in os.listdir(checkpoints_dir):
        if filename.startswith(best_model_prefix):
            best_model_filename = filename
            break  # Assuming only one best model checkpoint
    return os.path.join(checkpoints_dir, best_model_filename) if best_model_filename else None

def main(scene_type,exp_type,seed):
    # Set the random seed for each iteration
    set_random_seed(seed, deterministic=True)
    cfg = Config.fromfile('./configs/RoCoG-v2/i3d_r50_rocog_real_'+scene_type+'_video.py')
    
    # Modify dataset type and path
    cfg.data_root = 'data/rocog_v2_gen'
    cfg.ann_file_train = 'data/rocog_v2_gen/annotations/real2real_'+scene_type+'_'+exp_type+'.txt'
    cfg.ann_file_val = 'data/rocog_v2_gen/annotations/real_'+scene_type+'_val_tsonly.txt'
    cfg.ann_file_test = 'data/rocog_v2_gen/annotations/real_'+scene_type+'_test.txt'


    cfg.train_dataloader.dataset.ann_file = cfg.ann_file_train
    cfg.val_dataloader.dataset.ann_file = cfg.ann_file_val
    cfg.test_dataloader.dataset.ann_file = cfg.ann_file_test

    cfg.train_dataloader.dataset.data_prefix.video = cfg.data_root
    cfg.val_dataloader.dataset.data_prefix.video  = cfg.data_root
    cfg.test_dataloader.dataset.data_prefix.video = cfg.data_root


    # Modify num classes of the model in cls_head
    cfg.model.cls_head.num_classes = 7

    # We can use the pre-trained model
    cfg.load_from = './checkpoints/i3d_imagenet-pretrained-r50_8xb8-32x2x1-100e_kinetics400-rgb_20220812-e213c223.pth'

    # Set up working dir to save files and logs.
    cfg.work_dir = './work_dirs/i3d/'+scene_type+'_'+exp_type+'_'+str(seed)+'/'

    # cfg.train_dataloader.batch_size = int(cfg.train_dataloader.batch_size / 1)
    # cfg.val_dataloader.batch_size = int(cfg.val_dataloader.batch_size / 1)
    cfg.optim_wrapper.optimizer.lr = cfg.optim_wrapper.optimizer.lr / 5
    cfg.train_cfg.max_epochs = 20

    cfg.train_dataloader.num_workers = 4
    cfg.val_dataloader.num_workers = 2
    cfg.test_dataloader.num_workers = 2

    # We can initialize the logger for training and have a look
    # at the final config used for training
    print(f'Config:\n{cfg.pretty_text}')

    # Create work_dir
    mmengine.mkdir_or_exist(osp.abspath(cfg.work_dir))

    # build the runner from config
    runner = Runner.from_cfg(cfg)

    # start training
    runner.train()

    # Find the best model checkpoint and load the model
    best_checkpoint = find_best_model_checkpoint(cfg.work_dir)

    if best_checkpoint:
        print("Best checkpoint found at:" + best_checkpoint)
        cfg.load_from = best_checkpoint
        # build the runner from config
        runner = Runner.from_cfg(cfg)
    else:
        print("Best checkpoint not found.")

    # test
    runner.test()

    torch.cuda.empty_cache()

    


if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen

    # Your list of seeds
    seeds = [11111, 22222, 33333, 44444, 55555]

    # Iterate over the seeds list using a loop
    for seed in seeds:
        # Scene type aerial data
        scene_type = 'air'
        
        # Train Original data
        exp_type = 'train_tsonly'
        main(scene_type,exp_type,seed)

        # Train all Motion all Appearance
        exp_type = 'aMaA'
        main(scene_type,exp_type,seed)
        
        person = ['S05', 'S07','S08']
        N = len(person)
        for i in range(N):
            # Train 1 Motion all Appearance
            exp_type = '1MaA_' + person[i]
            main(scene_type,exp_type,seed)

            # Train all Motion 1 Appearance
            exp_type = 'aM1A_' + person[i]
            main(scene_type,exp_type,seed)

        # Scene type ground data
        scene_type = 'ground'

        # Train Original data
        exp_type = 'train_tsonly'
        main(scene_type,exp_type,seed)
        
        # Train all Motion all Appearance
        exp_type = 'aMaA'
        main(scene_type,exp_type,seed)
        
        person = ['S01','S03','S05', 'S07', 'S08']
        N = len(person)
        for i in range(N):
            # Train 1 Motion all Appearance
            exp_type = '1MaA_' + person[i]
            main(scene_type,exp_type,seed)

            # Train all Motion 1 Appearance
            exp_type = 'aM1A_' + person[i]
            main(scene_type,exp_type,seed)
        