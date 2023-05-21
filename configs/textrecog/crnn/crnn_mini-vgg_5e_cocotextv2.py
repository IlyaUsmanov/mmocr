_base_ = [
    '../_base_/datasets/cocotextv2.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_adadelta_5e.py',
    '_base_crnn_mini-vgg.py',
]
# dataset settings
cocotextv2_textdet_train = _base_.cocotextv2_textrecog_train
cocotextv2_textdet_train.pipeline = _base_.train_pipeline
cocotextv2_textdet_test = _base_.cocotextv2_textrecog_test
cocotextv2_textdet_test.pipeline = _base_.test_pipeline

default_hooks = dict(logger=dict(type='LoggerHook', interval=5000), )
train_dataloader = dict(
    batch_size=4,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=cocotextv2_textdet_train)

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=cocotextv2_textdet_test)

val_dataloader = test_dataloader

auto_scale_lr = dict(base_batch_size=4 * 4)
