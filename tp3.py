#Création d'une vidéos à partir d'images dans un dossier

import cv2
import os

# Dossier contenant les frames
frames_dir = "TP3 data/frames/"
output_video = "TP3 data/sortie/TP3_data_video.mp4"

# Récupérer et trier les images par numéro
images = sorted([img for img in os.listdir(frames_dir) if img.startswith("frame") and img.endswith(".jpg")],
                key=lambda x: int(x.replace("frame", "").replace(".jpg", "")))

# Vérifier si on a des images
if not images:
    print("Aucune image trouvée !")
else:
    # Charger la première image pour obtenir la taille
    frame = cv2.imread(os.path.join(frames_dir, images[0]))
    h, w, _ = frame.shape
    # Définir le codec et créer l'objet VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec pour MP4
    fps = 30  # Images par seconde
    out = cv2.VideoWriter(output_video, fourcc, fps, (w, h))

    # Ajouter chaque frame à la vidéo
    for img in images:
        frame = cv2.imread(os.path.join(frames_dir, img))
        out.write(frame)

    # Libérer la mémoire
    out.release()
    print(f" Vidéo créée avec succès : {output_video}")