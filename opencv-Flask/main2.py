# face recongition on pretrained images
from flask import Flask, render_template, redirect, Response, url_for
import cv2
import face_recognition
import numpy as np


