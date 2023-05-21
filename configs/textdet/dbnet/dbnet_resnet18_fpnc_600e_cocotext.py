_base_ = [
    '_base_dbnet_resnet18_fpnc.py',
    '../_base_/datasets/cocotextv2.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_adam_600e.py',
]

# dataset settings
cocotextv2_textdet_train = _base_.cocotextv2_textdet_train
cocotextv2_textdet_train.pipeline = _base_.train_pipeline
cocotextv2_textdet_test = _base_.cocotextv2_textdet_test
cocotextv2_textdet_test.pipeline = _base_.test_pipeline

train_dataloader = dict(
    batch_size=16,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=cocotextv2_textdet_train)

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=cocotextv2_textdet_test)

test_dataloader = val_dataloader

auto_scale_lr = dict(base_batch_size=4)
