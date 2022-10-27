RESIZE_DIM=64

data_dir='dataset'
#data_dir=os.path.join('..','input')
paths_aaj=glob.glob(os.path.join(data_dir,'aaj','*.jpg'))
paths_ami=glob.glob(os.path.join(data_dir,'ami','*.jpg'))
paths_badha=glob.glob(os.path.join(data_dir,'badha','*.jpg'))
paths_bondhu=glob.glob(os.path.join(data_dir,'bondhu','*.jpg'))
paths_tahara=glob.glob(os.path.join(data_dir,'tahara','*.jpg'))
paths_ashirbad=glob.glob(os.path.join(data_dir,'ashirbad','*.jpg'))
paths_bagh=glob.glob(os.path.join(data_dir,'bagh','*.jpg'))
paths_bati=glob.glob(os.path.join(data_dir,'bati','*.jpg'))
paths_detective=glob.glob(os.path.join(data_dir,'detective','*.jpg'))
paths_puru=glob.glob(os.path.join(data_dir,'puru','*.jpg'))
#paths_gram=glob.glob(os.path.join(data_dir,'gram','*.jpg'))
#paths_jail=glob.glob(os.path.join(data_dir,'jail','*.jpg'))
#paths_porishkar=glob.glob(os.path.join(data_dir,'porishkar','*.jpg'))
#paths_puru=glob.glob(os.path.join(data_dir,'puru','*.jpg'))
#paths_onurodh=glob.glob(os.path.join(data_dir,'onurodh','*.jpg'))
#paths_shomoy=glob.glob(os.path.join(data_dir,'shomoy','*.jpg'))

#paths_=glob.glob(os.path.join(data_dir,'','*.jpg'))

paths_train_all=paths_aaj+paths_ami+paths_badha+paths_bondhu+paths_tahara+paths_ashirbad+paths_bagh+paths_bati+paths_detective+paths_puru
#+paths_gram+paths_jail+paths_porishkar+paths_puru+paths_onurodh+paths_shomoy


label_aaj=os.path.join(data_dir,'aaj.csv')
label_ami=os.path.join(data_dir,'ami.csv')
label_badha=os.path.join(data_dir,'badha.csv')
label_bondhu=os.path.join(data_dir,'bondhu.csv')
label_tahara=os.path.join(data_dir,'tahara.csv')
label_ashirbad=os.path.join(data_dir,'ashirbad.csv')
label_bagh=os.path.join(data_dir,'bagh.csv')
label_bati=os.path.join(data_dir,'bati.csv')
label_detective=os.path.join(data_dir,'detective.csv')
label_puru=os.path.join(data_dir,'puru.csv')
#label_gram=os.path.join(data_dir,'gram.csv')
#label_jail=os.path.join(data_dir,'jail.csv')
#label_porishkar=os.path.join(data_dir,'porishkar.csv')
#label_puru=os.path.join(data_dir,'puru.csv')
#label_onurodh=os.path.join(data_dir,'onurodh.csv')
#label_shomoy=os.path.join(data_dir,'shomoy.csv')
#label_=os.path.join(data_dir,'.csv')