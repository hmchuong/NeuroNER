export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
python3 main.py --train_model=False --use_pretrained_model=True --dataset_text_folder=../data/example_unannotated_texts --pretrained_model_folder=../trained_models/conll_2003_en
