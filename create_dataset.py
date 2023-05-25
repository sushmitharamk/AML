def create_directories(newpath,dataset_path):
    for i in os.listdir(dataset_path):
        os.chdir(newpath)
        os.mkdir(i)
    

def convert_images_to_videos(dataset_path):
    for labeldir in os.listdir(daatset_path):
    labelpath=os.path.join(dataset_path,labeldir)
    for i,id in enumerate(os.listdir(labelpath)):
      imgpath=os.path.join(labelpath,id)
      print(imgpath)
      if os.listdir(imgpath)==[]:
        print("empty dir")
        continue
      try:
        video = ImgSeqClip.ImageSequenceClip(sorted(glob.glob(os.path.join(imgpath, '*.jpg'))), fps=32)
        path=os.path.join(videos_path,labeldir)
        os.chdir(path)
        video.write_videofile(str(i+1)+'.mp4')
      except:
        continue

dataset_path="/content/drive/MyDrive/aml/HMDB_simp/" #your dataset path which contains all the label folders
new_path="/content/drive/MyDrive/aml/data/"
create_directories(new_path,dataset_path)
convert_images_to_videos(dataset_path)

