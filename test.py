from parsing import parse_train_args
from cv import cv
from utils import create_logger






if __name__ == '__main__':
    args = parse_train_args()

    args.num_folds=1
    args.epochs=1
    args.ensemble_size=2
    args.batch_size=128

    args.activation='ReLU'
    args.depth=3
    args.dropout=0
    args.ffn_num_layers=3
    args.hidden_size=150
    args.sumstyle=True
    args.seed=42
    args.gpuUSE=False




    args.data_path,args.cols_to_read ='data_RE2/solv_logp.csv',[x for x in range(3)]


    args.save_dir='save_test'

    args.tmp_data_dir='./data_RE2/tmp/'
    args.scale='normalization'

    args.dataset_type, args.metric='regression','rmse'


    args.class_balance=True
    args.split_type='random'




    args.diff_depth_weights=True
    args.layers_per_message=1


    args.attention=False
    args.message_attention=False
    args.global_attention=False
    args.message_attention_heads=1
    args.log_dir=None

    print(args)
    logger = create_logger(name='train_crossValidate', save_dir=args.save_dir, quiet=args.quiet)



    cv(args, logger)









