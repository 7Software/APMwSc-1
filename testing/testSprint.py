# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo sprintClass.py
sys.path.append('../app/scrum')

from sprintClass import *
from accions     import *
from category    import *
from task        import *

class TestSprintClass(unittest.TestCase):

    def setUp(self):
        # Insertamos los datos necesarios.
        self.aBacklog  = backlog()
        self.aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId         = self.aBacklog.findName('Bxtyllz')
        self.idBacklog = findId[0].BL_idBacklog

    def tearDown(self):
        # Eliminamos los datos insertados.
        self.aBacklog.deleteProduct('Bxtyllz')

    #############################################
    #         Pruebas para insertSprint         #
    #############################################
 
    # Caso Inicial
    # Prueba 1
    def testInsertSprintExists(self):
        aSprint      = sprints()
        aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Casos Normales
 
    # Prueba 2
    def testInsertSprintElement(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba 3
    def testInsertSprintRepeatedNumber(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        result1   = aSprint.insertSprint(1,'Haskndwkd akdmkwdmdwa',self.idBacklog)
        self.assertFalse(result1)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Casos Fronteras
 
    # Prueba 4
    def testInsertSprintShortDesc0(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,'',self.idBacklog)
        self.assertFalse(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba 5
    def testInsertSprintLongDesc1(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,'@',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba 6
    def testInsertSprintLongDesc140(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba 7
    def testInsertSprintLongDesc141(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,20*'LlWmcrl' + 'x',self.idBacklog)
        self.assertFalse(result)
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba 8
    def testInsertSprintIdBackLogInvalid(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Wtqczr ul mds dfbyl',0)
        self.assertFalse(result)
 
    # Casos Esquinas
 
    # Prueba 9
    def testInsertSprintIdBacklogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'DwfEndqr cun fw3rzv',80)
        self.assertFalse(result)
 
    # Prueba 10
    def testInsertSprintLongDesc140AndIdBackLogNoExists(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,20*'LlWmcrl',99)
        self.assertFalse(result)
 
    def testInsertMaxSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER,'MAX_SPRINT_TEST',self.idBacklog)
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(MAX_SPRINT_NUMBER,self.idBacklog)
 
    # Casos Maliciosos
 
    # Prueba
    def testInsertNotString(self):
        aSprint   = sprints()
        result    = aSprint.insertSprint(1,4350,self.idBacklog)
        self.assertFalse(result)
 
    # Prueba
    def testInsertNoneAsString(self):
        aSprint      = sprints()
        result    = aSprint.insertSprint(1,None,self.idBacklog)
        self.assertFalse(result)
 
    # Prueba
    def testInsertIdNegative(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Nxn3zzzz',-1)
        self.assertFalse(result)
 
    # Prueba
    def testInsertIdAsString(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(1,'Nxn3zzzz','1')
        self.assertFalse(result)
 
    def testInsertNegativeSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(-1,'Nxn3zzzz',self.idBacklog)
        self.assertFalse(result)
 
    def testInsertMaxOverflowSprintNumber(self):
        aSprint  = sprints()
        result   = aSprint.insertSprint(MAX_SPRINT_NUMBER+1,'Nxn3zzzz',self.idBacklog)
        self.assertFalse(result)
 
    #############################################      
    #       Pruebas para searchIdSprint         #
    #############################################  
    # Caso Inicial
 
    # Prueba
    def testsearchIdSprintExists(self):
        # Insertamos los datos necesarios.
        aSprint        = sprints()
        aSprint.insertSprint(1,'VsAr cdmzndqs qspxcywlts',self.idBacklog)
        # Inicio de la prueba.
        foundSprint = aSprint.searchIdSprint(1, self.idBacklog)[0]
        self.assertEqual(foundSprint.S_sprintDescription, 'VsAr cdmzndqs qspxcywlts')
        self.assertEqual(foundSprint.S_numero, 1)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('VsAr cdmzndqs qspxcywlts',self.idBacklog)
 
    # Caso Normal
 
    # Prueba
    def testSearchIdNotExist(self):
        # Insertamos los datos necesarios.
        aSprint        = sprints()
        aSprint.insertSprint(1,'VsAr cdmzndqs qspxcywlts',self.idBacklog)
        # Inicio de la prueba.
        foundSprintId = aSprint.searchIdSprint(100, self.idBacklog)
        self.assertEqual(foundSprintId,[])
        # Eliminamos los datos insertados.
        aSprint.deleteSprint('VsAr cdmzndqs qspxcywlts',self.idBacklog)
 
    # Prueba
    def testSearchIdNoBacklog(self):
        # Inicio de la prueba. 
        aSprint     = sprints()
        result   = aSprint.searchIdSprint(1, None)
        self.assertEqual(result,[],"Elemento no encontrado")
 
    # Casos Maliciosos
    # Prueba
    def testSearchIdInvalid(self):
        # Inicio de la prueba.
        aSprint     = sprints()
        result   = aSprint.searchIdSprint(0,self.idBacklog)
        self.assertEqual(result,[],"Elemento no encontrado")
 
    # Prueba
    def testSearchIdString(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint('',self.idBacklog)
        self.assertEqual(result,[],"Elemento no encontrado")
 
    # Prueba
    def testSearchIdNoneString(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint(1, None)
        self.assertEqual(result,[],"Válido")
 
    # Prueba
    def testSearchIdNegative(self):
        # Inicio de la prueba.
        aSprint  = sprints()
        result   = aSprint.searchIdSprint(-1, self.idBacklog)
        self.assertEqual(result,[],"Válido")
 
    #############################################
    #        Pruebas para updateSprint          #
    #############################################  
 
    # Caso Inicial
 
    # Prueba
    def testupdateSprintExists(self):
        aSprint      = sprints()
        aSprint.insertSprint(1,'Yntdcvr an miqn',self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 2 , 'Tnbdc3r xrmq asrtdmp')
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        aSprint.deleteSprint(2,self.idBacklog)
 
    # Casos Normales
    # Prueba
    def testupdateSprintDesc(self):
        aSprint   = sprints()
        aSprint.insertSprint(1,'Altomy Tnvfcgcyqn',self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 1 , 'Tnbdc3r xrmq asrtdmp')
        sprintUpdate = aSprint.searchIdSprint(1,self.idBacklog)[0]
        self.assertEqual(sprintUpdate.S_sprintDescription, 'Tnbdc3r xrmq asrtdmp')
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba
    def testupdateSprintNumber(self):
        aSprint   = sprints()
        aSprint.insertSprint(1,'Altomy Tnvfcgcyqn', self.idBacklog)
        aSprint.updateSprint(1, self.idBacklog, 2 ,'Altomy Tnvfcgcyqn')
        sprintUpdate = aSprint.searchIdSprint(2,self.idBacklog)[0]
        self.assertNotEqual(sprintUpdate, [])
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
        aSprint.deleteSprint(2,self.idBacklog)
 
    # Prueba
    def testupdateSprintDescNOtExist(self):
        aSprint      = sprints()
        result = aSprint.updateSprint(1, self.idBacklog, 2 ,'Altomy Tnvfcgcyqn')
        self.assertFalse(result)
 
    # Casos Fronteras
 
    # Prueba
    def testupdateSprintLeftLen1(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog,1,'Bvscqr pontfs ddbyl3z')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba
    def testupdateSprintRightLong1(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,'@')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba
    def testupdateSprintRightLen140(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,140*'T')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba
    def testupdateSprintLeftLen140(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, 140*'T', self.idBacklog)
        result    = aSprint.updateSprint(1, self.idBacklog, 1,'@jutdr tqdf lu mpgya')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aSprint.deleteSprint(1,self.idBacklog)
 
    # Prueba
    def testupdateSprintIdBackLogInvalid(self):
        aSprint   = sprints()
        aSprint.insertSprint(1, '@jutdr tqdf lu mpgya', self.idBacklog)
        result    = aSprint.updateSprint(1,'', 1, 'Wtqczr ul mds dfbyl')
        self.assertFalse(result)
 
    #############################################
    #         Pruebas para deleteSprint         #
    #############################################
 
    # Caso Inicial
 
    # Prueba
    def testDeletSprintExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
        result   = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        oSprint.deleteSprint(1,self.idBacklog)
 
 
    # Casos Normales
 
    # Prueba
    def testDeleteValidSprint(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(2,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(2,self.idBacklog)
        self.assertTrue(result)
 
 
    # Casos Fronteras internas
  
    # Prueba
    def testDeleteSprintNum1ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1,self.idBacklog)
        self.assertTrue(result) 
 
    #Prueba
    def testDeleteSprintNum1000ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1000,self.idBacklog)
        self.assertTrue(result)
 
     
    # Casos Fronteras internas
 
    #Prueba
    def testDeleteSprintNum0ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(0,self.idBacklog)
        self.assertFalse(result)  
 
    #Prueba
    def testDeleteSprintNum1001ValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(1001,self.idBacklog)
        self.assertFalse(result) 
 
    #Prueba
    def testDeleteSprintNegativeNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(-1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(-1,self.idBacklog)
        self.assertFalse(result) 
 
    #Prueba
    def testDeleteSprintStringNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint('1','VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint('1',self.idBacklog)
        self.assertFalse(result) 
 
    #Prueba
    def testDeleteSprintNullNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        result   = oSprint.insertSprint(None,'VtXcyr pvntgs dw wydz',self.idBacklog)
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(None,self.idBacklog)
        self.assertFalse(result) 
     
    #Prueba
    def testDeleteSprintNotNumValidIdBacklog(self):
        # Insertamos los datos necesarios.
        oSprint  = sprints()
        # Inicio de la prueba.
        result   = oSprint.deleteSprint(100,self.idBacklog)
        self.assertFalse(result)
 
    #############################################
    #      Pruebas para asignSprintHistory      #
    #############################################
 
    #Caso Inicial
 
    #Prueba
    def testAsignSprintHistoryExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,idFound)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    # Casos normales
 
    # Prueba 
    def testAsignSprintHistoryValidElements(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(5,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(5,self.idBacklog,idFound)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(5,self.idBacklog,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos frontera interna
 
    # Prueba 
    def testAsignSprintHistoryNumberMin(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,idFound)
        self.assertTrue(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryNumberMax(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1000,self.idBacklog,idFound)
        self.assertTrue(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1000,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos frontera externa
 
    # Prueba 
    def testAsignSprintHistoryNumberZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(0,self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(0,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryNumberMaxOut(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1001,self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1001,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryIdBacklogZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,0,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1,0,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryUserHIstoryZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,0)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,0)
 
    #Casos Maliciosos
 
    # Prueba 
    def testAsignSprintHistoryNumberNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1002,self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        oSprint.deleteAssignedSprintHistory(1002,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryNumberString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory('1',self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory('1',self.idBacklog,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryNumberNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(None,self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(None,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryNumberNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(-1,self.idBacklog,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,idFound)
        oSprint.deleteAssignedSprintHistory(-1,self.idBacklog,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryBacklogNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,1001,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,1001,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryBacklogString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,'1',idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,'1',idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryBacklogNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,None,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,None,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryBacklogNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,-1,idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,-1,idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryIdUserHistoryNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,1001)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,1001)
        oSprint.deleteSprint(1,self.idBacklog)
 
    #Prueba
    def testAsignSprintHistoryIdUserHistoryString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,str(idFound))
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,str(idFound))
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testAsignSprintHistoryIdUserHistoryNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,None)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,None)
        oSprint.deleteSprint(1,self.idBacklog)
 
    #Prueba
    def testAsignSprintHistoryIdUserHistoryNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Inicio de la prueba.
        result = oSprint.asignSprintHistory(1,self.idBacklog,-idFound)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,-idFound)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #############################################
    #   Pruebas para getAssignedSprintHistory   #
    #############################################
 
    #Caso inicial
 
    #Prueba
    def testGetAssignedSprintHistoryExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
         
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
         
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
         
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,self.idBacklog)
        self.assertTrue(result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(5,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    #Caso normal
 
    #Prueba
    def testGetAssignedSprintHistoryValidElements(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(5,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(5,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(5,self.idBacklog)
        self.assertNotEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(5,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(5,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    #Casos frontera interna
 
    #Prueba
    def testGetAssignedSprintHistoryNumberMin(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,self.idBacklog)
        self.assertNotEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryNumberMax(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1000,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1000,self.idBacklog)
        self.assertNotEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1000,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1000,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    #Casos frontera externa
 
    #Prueba
    def testGetAssignedSprintHistoryNumberZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(0,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(0,self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(0,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(0,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryNumberMaxOut(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1001,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1001,self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1001,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1001,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryidBacklogZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,0,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,0)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1,0,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos maliciosos
 
    #Prueba
    def testGetAssignedSprintHistoryNumNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1002,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1002,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1002,self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1002,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1002,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    #Prueba
    def testGetAssignedSprintHistoryNumString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory('1',self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory('1',self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory('1',self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryNumNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(None,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(None,self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(None,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryNumNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(-1,self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(-1,self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(-1,self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryIdBacklogString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,str(self.idBacklog),idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,str(self.idBacklog))
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1,str(self.idBacklog),idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryIdBacklogNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,None,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,None)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1, None,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testGetAssignedSprintHistoryIdBacklogNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,-self.idBacklog,idFound)
 
        # Inicio de la prueba.
        result = oSprint.getAssignedSprintHistory(1,-self.idBacklog)
        self.assertEqual([],result)
 
        #Eliminamos los elementos creado
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintHistory(1,-self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #############################################
    #      Pruebas para asignSprintTask         #
    #############################################
 
    #Caso Inicial
 
    #Prueba
    def testAsignSprintTaskExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(7,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
      
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(7,self.idBacklog,idFoundT)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(7,self.idBacklog,idFoundT)
        oSprint.deleteSprint(7,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Casos normales
 
    # Prueba 
    def testAsignSprintTaskValidElements(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(6,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(6,self.idBacklog,idFoundT)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(6,self.idBacklog,idFoundT)
        oSprint.deleteSprint(6,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos frontera interna
 
    # Prueba 
    def testAsignSprintTaskSprintNumberMin(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,self.idBacklog,idFoundT)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskSprintNumberMax(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1000,self.idBacklog,idFoundT)
        self.assertTrue(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1000,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1000,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos frontera externa
 
    # Prueba 
    def testAsignSprintTaskSprintNumberZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(0,self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(0,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskSprintNumberMaxOut(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1001,self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1001,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1001,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    # Prueba 
    def testAsignSprinTaskIdBacklogZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(2,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(2,0,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia y la accion creado
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(2,0,idFoundT)
        oSprint.deleteSprint(2,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskIdTaskZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(3,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(3,self.idBacklog,0)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(3,self.idBacklog,0)
        oSprint.deleteSprint(3,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Casos Maliciosos
 
    # Prueba 
    def testAsignSprintTaskSprintNumberNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1002,self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1002,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskSprintNumberString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(str(idFound),self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(str(idFound),self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskSprintNumberNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(None,self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(None,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskSprintNumberNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(-idFoundT,self.idBacklog,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(-idFoundT,self.idBacklog,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
 
    # Prueba 
    def testAsignSprintTaskBacklogNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,1001,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,1001,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskBacklogString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,'1',idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,'1',idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskBacklogNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,None,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,None,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintTaskBacklogNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,-1,idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,-1,idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    # Prueba 
    def testAsignSprintHistoryIdTaskNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,self.idBacklog,1001)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,1001)
        oSprint.deleteSprint(1,self.idBacklog)
 
    #Prueba
    def testAsignSprintHistoryIdTaskString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,self.idBacklog,str(idFoundT))
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,str(idFoundT))
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
 
    #Prueba
    def testAsignSprintHistoryIdTaskNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,self.idBacklog,None)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,None)
        oSprint.deleteSprint(1,self.idBacklog)
 
    #Prueba
    def testAsignSprintHistorySprintIdUserHistoryNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()
 
        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
 
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
 
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
 
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
 
        # Inicio de la prueba.
        result = oSprint.asignSprintTask(1,self.idBacklog,-idFoundT)
        self.assertFalse(result)
 
        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,-idFoundT)
        oSprint.deleteSprint(1,self.idBacklog)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)
        
    #############################################
    #   Pruebas para getAssignedSprintTask      #
    #############################################

    #Caso inicial

    #Prueba
    def testGetAssignedSprintTaskExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)
        
        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion
        
        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask
        
        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,self.idBacklog)
        self.assertTrue(result)

        #Eliminamos la historia, la accion y el sprint creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Caso normal

    #Prueba
    def testGetAssignedSprintTaskValidElements(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(5,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(5,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(5,self.idBacklog)
        self.assertNotEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(5,self.idBacklog)
        oSprint.deleteAssignedSprintTask(5,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Casos frontera interna

    #Prueba
    def testGetAssignedSprintTaskNumberMin(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,self.idBacklog)
        self.assertNotEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskNumberMax(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1000,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1000,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1000,self.idBacklog)
        self.assertNotEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1000,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1000,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)


    #Casos frontera externa

    #Prueba
    def testGetAssignedSprintTaskNumberZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(0,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(0,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(0,self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(0,self.idBacklog)
        oSprint.deleteAssignedSprintTask(0,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskNumberMaxOut(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1001,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1001,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1001,self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1001,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1001,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskidBacklogZero(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintHistory(1,0,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,0)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1,0,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Casos maliciosos

    #Prueba
    def testGetAssignedSprintTaskNumNotExists(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1002,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1002,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1002,self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1002,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1002,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)


    #Prueba
    def testGetAssignedSprintTaskNumString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask('1',self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask('1',self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask('1',self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskNumNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(None,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(None,self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(None,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintHistoryNumNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(-1,self.idBacklog,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(-1,self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(-1,self.idBacklog,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskIdBacklogString(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1,str(self.idBacklog),idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,str(self.idBacklog))
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1,str(self.idBacklog),idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskIdBacklogNone(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1,None,idFoundT)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,None)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1, None,idFoundT)
        oHistory.deleteUserHistory(idFound)
        oAccion.deleteAccion('Dxfynyr',self.idBacklog)

    #Prueba
    def testGetAssignedSprintTaskIdBacklogNegative(self):
        # Insertamos los datos necesarios. 
        oSprint  = sprints()

        #Creamos un nuevo sprint
        result1  = oSprint.insertSprint(1,'VtXcyr pvntgs dw wydz',self.idBacklog)

        #Creamos una nueva historia de usuario
        #Insertamos la accion
        oAccion = accions()
        oAccion.insertAccion('Dxfynyr', self.idBacklog)
        search  = oAccion.searchAccion('Dxfynyr', self.idBacklog)
        idFound = search[0].AC_idAccion

        #Insertamos la historia
        oHistory = userHistory()
        result   = oHistory.insertUserHistory('jDw',0,1,idFound,self.idBacklog,1)
        search  = oHistory.searchUserHistory('jDw',self.idBacklog)
        idFound = search[0].UH_idUserHistory
        
        # Insertamos la categoria
        aCategory = category()
        aCategory.insertCategory('wofhweoifh',1)
 
        # Insertamos la tarea    
        aTarea  = task()
        result3 = aTarea.insertTask('dwidjw',1,1,idFound)
        search  = aTarea.searchTask('dwidjw')
        idFoundT = search[0].HW_idTask

        #Asignamos la historia al sprint
        result2 = oSprint.asignSprintTask(1,-self.idBacklog,idFound)

        # Inicio de la prueba.
        result = oSprint.getAssignedSprintTask(1,-self.idBacklog)
        self.assertEqual([],result)

        #Eliminamos los elementos creado
        aTarea.deleteTask('dwidjw')
        aCategory.deleteCategory('wofhweoifh')
        oSprint.deleteSprint(1,self.idBacklog)
        oSprint.deleteAssignedSprintTask(1,-self.idBacklog,idFound)
        oHistory.deleteUserHistory(idFound)