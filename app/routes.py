from flask import Blueprint, request
import ntplib
from app.functions import encrypt_dictoniary, decrypt_dictoniary
from app.models import Copies, Versions
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/API', methods=['POST'])
def API():
    match (decrypt_dictoniary(request.json)['type']):
        case 'check':
            copy = Copies.query.filter_by(serial=decrypt_dictoniary(request.json)['serial'], uuid=decrypt_dictoniary(request.json)['uuid']).first()
            version = Versions.query.filter_by(version=decrypt_dictoniary(request.json)['version'], sha256=decrypt_dictoniary(request.json)['sha256']).first()
            if copy is None or version is None:
                return encrypt_dictoniary({"message": "copy_verification_error"})

            return encrypt_dictoniary({"message": "status_OK",
                                       "timestamp": str(ntplib.NTPClient().request('time.google.com', version=3).tx_time)})
        
        case 'register':
            copy = Copies.query.filter_by(serial=decrypt_dictoniary(request.json)['serial']).first()
            if copy is None:
                return encrypt_dictoniary({"message": "copy_not_exist"})
            
            if copy.uuid != "":
                return encrypt_dictoniary({"message": "copy_already_registered"})
            
            copy.uuid = decrypt_dictoniary(request.json)['uuid']
            db.session.commit()
            return encrypt_dictoniary({"message": "copy_registered_succesfully"})
        
        case 'uninstall':
            copy = Copies.query.filter_by(serial=decrypt_dictoniary(request.json)['serial'], uuid=decrypt_dictoniary(request.json)['uuid']).first()
            if copy is None:
                return encrypt_dictoniary({"message": "copy_not_exist"})
            
            copy.uuid = ""
            db.session.commit()
            return encrypt_dictoniary({"message": "copy_uninstalled"})

        case '99_luftballons':
            return encrypt_dictoniary({"message": "es_ist_ein_ufo!"})

        case _:
            return encrypt_dictoniary({"message": "error_wrong_request_type"})