# -*- coding: utf-8 -*-. 

import sys
import datetime
from sqlalchemy import DateTime 
# Ruta que permite utilizar el módulo backlog.py
sys.path.append('app/scrum')

from sprintClass import *
from meetingClass import *

# Declaracion de constantes.
MIN_ID_MEETING = 1

MIN_ELEMENT_CHALLENGES = 1
MAX_ELEMENT_CHALLENGES = 300

MIN_ELEMENT_PLANNED = 1
MAX_ELEMENT_PLANNED = 300

MIN_ELEMENT_DONE = 1
MAX_ELEMENT_DONE = 300

class elementMeeting(object):

	def emptyTable(self):
		'''Permite saber si la tabla elementMeeting esta vacia'''
		aElement = clsElementMeeting.query.all()
		return (aElement == [])

	def getElementID(self,idElement,idMeeting):
		aMeeting = clsElementMeeting.query.filter_by(EM_meeting = idMeeting, EM_idElementMeeting = idElement).all()
		return (aMeeting)

	def insertElement(self, challenges, planned, done, idMeeting, user):
		'''Permite insertar un elemento a una reunión diaria'''   
		checkTypeChallenges     = type(challenges) == str
		checkTypePlanned	    = type(planned) == str
		checkTypeDone		    = type(done) == str
		checkTypeIdMeeting		= type(idMeeting) == int

		# Verifica que la longitud de los campos sea correcta
		if checkTypeChallenges and checkTypePlanned and checkTypeDone and checkTypeIdMeeting:
			
			checkChallengeLong = MIN_ELEMENT_CHALLENGES <= len(challenges) <= MAX_ELEMENT_CHALLENGES
			checkPlannedLong   = MIN_ELEMENT_PLANNED <= len(planned) <= MAX_ELEMENT_PLANNED
			checkDoneLong 	   = MIN_ELEMENT_DONE <= len (done) <= MAX_ELEMENT_DONE
			checkIdMeeting 	   = MIN_ID_SPRINT <= idMeeting

			# Si todas las longitudes son correctas
			if checkChallengeLong and checkPlannedLong and checkDoneLong and checkIdMeeting:

				# Verifico que el meeting exista
				foundMeeting = clsSprintMeeting.query.filter_by(SM_idSprintMeeting = idMeeting)
			
				# Si el meeting existe. Verifico que usuario no se repita
				if foundMeeting != []:

					foundElement = clsElementMeeting.query.filter_by(EM_meeting = idMeeting, EM_user= user)
					
					# Si no hay ninguna element en esa reunión con ese usuario
					if foundElement == []:
						newElement = clsElementMeeting(challenges,planned, done, idMeeting, user)
						db.session.add(newElement)
						db.session.commit()
						return True
		return False

	def updateElement(self, elementId, newChallenges, newPlanned, newDone, idMeeting, user):
		'''Permite editar un elemento a una reunión diaria'''   
		checkTypeChallenges     = type(newChallenges) == str
		checkTypePlanned	    = type(newPlanned) == str
		checkTypeDone		    = type(newDone) == str
		checkTypeIdMeeting		= type(idMeeting) == int

		# Verifica que la longitud de los campos sea correcta
		if checkTypeChallenges and checkTypePlanned and checkTypeDone and checkTypeIdMeeting:
			
			checkChallengeLong = MIN_ELEMENT_CHALLENGES <= len(newChallenges) <= MAX_ELEMENT_CHALLENGES
			checkPlannedLong   = MIN_ELEMENT_PLANNED <= len(newPlanned) <= MAX_ELEMENT_PLANNED
			checkDoneLong 	   = MIN_ELEMENT_DONE <= len (newDone) <= MAX_ELEMENT_DONE
			checkIdMeeting 	   = MIN_ID_SPRINT <= idMeeting

			foundElement = self.getElementID(elementId,idMeeting)

			if foundElement != []:
				foundElement[0].EM_challenges = newChallenges
				foundElement[0].EM_planned = newPlanned
				foundElement[0].EM_done = newDone

				db.session.commit()
				return True

		return False


	def deleteMeeting(self,elementId, idSprint):
		'''Permite eliminar una elemento de una reunión'''

		foundElement = self.getElementID(elementId,idMeeting)
		if foundElement !=[]:
			for m in foundElement:
				db.session.delete(m)
			db.session.commit()
			return True
		return False

		




