# -*- coding: utf-8 -*-
#ZRC 2023/1/4

from pyfbsdk import *
from pyfbsdk_additions import *
import xml.etree.ElementTree as ET
import json
#import _winreg
import os

#元数据镜头文本
shogunMetadataText=r"E:\Script\AnimationExport\MBExportMetadataText.txt"
bodyPath={
#玩家女
'PC_F':r"Z:\AnimGroup\Rigging\Avatar\CharSet\30300000015\ALLBody\Char_Angle_Rig_MG_Char.fbx",
#玩家男
#'PC_M':"Z:\AnimGroup\Rigging\NPC\NPC_IecBear\NPC_IceBear_Rig_MG_Char.fbx",
#万飞
'WanFei':r"Z:\AnimGroup\Rigging\Avatar\CharSet\30300000013\ALLBody\Wanfei_UI_Rig_MG_Char.fbx",
#金医生
"DrJin":r"Z:\AnimGroup\Rigging\NPC\NPC_DrJin\NPC_DrJin_Rig_MG_Char.fbx",
#冰熊
"IceBear":r"Z:\AnimGroup\Rigging\NPC\NPC_IecBear\NPC_IceBear_Rig_MG_Char.fbx",
#歼灭者
'Annihilator':r"Z:\AnimGroup\Rigging\AICharacters\Boss_CPN_AnnihilatorProto\Boss_CPN_AnnihilatorProto_Rig_MG_Char.fbx",
#飓风军团NPC

'NPC_HeavyArmor_Soldier_3':r'Z:\AnimGroup\Rigging\NPC\NPC_HeavyArmor_Soldier_3\NPC_HeavyArmor_Soldier_3_Rig_MG_Char.fbx',
'NPC_HeavyArmor_Soldier_2':r'Z:\AnimGroup\Rigging\NPC\NPC_HeavyArmor_Soldier_2\NPC_Hurricane_Soldier_2_Rig_MG_Char.fbx',
'NPC_HeavyArmor_Soldier_1':r'Z:\AnimGroup\Rigging\NPC\NPC_HeavyArmor_Soldier_1\NPC_Hurricane_Soldier_1_Rig_MG_Char.fbx'
}
CharList=['PC_F_Char',
'WanFei_Char',
'DrJin_Char',
"IceBear_Char",
'Annihilator_Char',
'NPC_HeavyArmor_Soldier_1_Char',
'NPC_HeavyArmor_Soldier_2_Char',
'NPC_HeavyArmor_Soldier_3_Char']

funcLogL='<<'
funcLogR='>>'
class MotionBuilderExportTool:
    def __init__(self):
        print('---------<Init>---------')
        CamePath=open(shogunMetadataText)
        
        self.shogunAnimalPathList=CamePath.read().split("\n")
        CamePath.close()
        self.tool = FBCreateUniqueTool('修改角色体插件')
        self.tool.StartSizeX = 200
        self.tool.StartSizeY = 300
        #窗口布局
        self.PopulateconfigLayout(self.tool)
 
        ShowTool(self.tool)
        #窗口销毁事件回调
        self.tool.OnUnbind.Add(self.OnToolDestroy)

        #MB文件地址
        self.motionBuilderAnimalPath=''

        self.saveAnimalFilePath=''
        self.characterBodyName=[]
        self.PropName=[]

        #角色
        self.CharInst=[]
        self.errorChar=[]
        self.CharOldList=[]
        print('---------<InitOver>---------')
    def OnToolDestroy(self, control, event):
        FBSystem().Scene.OnChange.Remove(SceneChanged)
    def PopulateconfigLayout(self, mainLayout):
        anchor = FBAttachType.kFBAttachTop
        anchorRegion = ""
        #配置大小区域
        x = FBAddRegionParam(10, FBAttachType.kFBAttachLeft, '')
        y = FBAddRegionParam(100, FBAttachType.kFBAttachTop, '')
        w = FBAddRegionParam(-10, FBAttachType.kFBAttachRight, '')
        h = FBAddRegionParam(100, FBAttachType.kFBAttachNone, '')
        mainLayout.AddRegion('Config', '', x, y, w, h)
        #创建纵向布局
        configLayout = FBVBoxLayout()
        mainLayout.SetControl('Config', configLayout)

       
        
        
    # Create label
        # labId = "Label" 
        # l = FBLabel()
        
        # x = FBAddRegionParam(10, FBAttachType.kFBAttachLeft, "")
        # y = FBAddRegionParam(10,  anchor,anchorRegion)
        # w = FBAddRegionParam(300, FBAttachType.kFBAttachNone, "")
        # h = FBAddRegionParam(25, FBAttachType.kFBAttachNone, "")
        # mainLayout.AddRegion(labId, labId, x, y, w, h)
        # mainLayout.SetControl(labId, l)

        Button_1 = FBButton()
       
        Button_1.OnClick.Add(self.Main1)
        Button_1.Caption = '更新角色体'
        configLayout.Add(Button_1, 50)

        Button_2 = FBButton()
       
        Button_2.OnClick.Add(self.Main)
        Button_2.Caption = '替换原有角色体'
        configLayout.Add(Button_2, 50)
    # def getMotionBuilderAnimalPath(self,temp):
    #     '''
    #     获取动画地址
    #     '''
    #     print('%sgetMotionBuilderAnimalPath%s'%(funcLogL,funcLogR))
    #     temp[7]='Take.MotionBuilder'
    #     temp.append('Work')        
        

    #    # tempStr.append('Output')
        
    #     self.motionBuilderAnimalPath=str('\\'.join(temp))
    #     print('MotionBuilderAnimalPath:|%s|'%self.motionBuilderAnimalPath)
    #     print('camName:<%s>'%self.camName)

    def getAnimalFileSavePath(self,temp):
        '''
        获取动画文件保存地址
        ''' 
        print('%sgetAnimalFileSavePath%s'%(funcLogL,funcLogR))


        #self.saveAnimalFilePath=
    # def getCharaterPropData(self,data):
    #     '''
    #     获取角色数据
    #     '''
    #     self.characterBodyName=[]
    #     self.PropName=[]
    #     print('%sgetCharaterData%s'%(funcLogL,funcLogR))
    #     for i in range(len(data["roleList"])):
            
    #         temp=data["roleList"][i]["blueprint"]["type"]
    #         print("type:%s"%temp)
    #         temp2=data["roleList"][i]["name"]
    #         if temp!='Camera':            
            
    #             if temp=="Character":                
    #                 self.characterBodyName.append(temp2)
    #                 print('Character:%s'%temp2)
    #             if temp=='RigidProp':
    #                 self.PropName.append(temp2)
    #                 print('RigidProp:%s'%temp2)
        
    #导入模型
    def MergeNewChar(self,charName,charPath):        
        mergeApp = FBApplication()        
        loadOption = FBFbxOptions(True,charPath)
        loadOption.NamespaceList = charName+'_Char_New'
        #loadOption.OwnerNamespace=self.charInstName
        for takeIndex in range( 0, loadOption.GetTakeCount() ):
        # 取消选择options
            loadOption.SetTakeSelect( takeIndex, False )
        mergeApp.FileMerge(charPath, False, loadOption)
        FBSystem().Scene.Evaluate()

    def openFile(self,path):

        print('%sLoadModelFile%s'%(funcLogL,funcLogR))
        targetFilepath = path+'\\'+self.camName+'.fbx'
        if targetFilepath == '':
            FBMessageBox( 'Config','没有模型文件路径', 'OK', None, None )
            return
        app = FBApplication()
        app.FileNew()
        loadOption = FBFbxOptions(True)
        
        
        app.FileOpen(targetFilepath, True, loadOption)

        FBSystem().Scene.Evaluate() 
    #烘焙动画
    def PlotSkeleton(self): 
        print('%sPlotSkeleton%s'%(funcLogL,funcLogR))
        currentCharacter = FBApplication().CurrentCharacter
        # # 禁用并删除控制Rig
        # currentCharacter.ActiveInput = False
        # controlRig = currentCharacter.GetCurrentControlSet()
        # # 如果没有控制Rig，就创建一个新的
        # if not controlRig:
        #     # 使用“True”参数指定的正运动学和逆运动学创建一个控制Rig
        #     bCreationResult = currentCharacter.CreateControlRig(True)
        #     if not bCreationResult:
        #         print('在PlotToControlRig中创建新的控制rig失败，请检查')
        
        plotOptions = FBPlotOptions()
        plotOptions.ConstantKeyReducerKeepOneKey = False
        plotOptions.PlotAllTakes = False 
        plotOptions.PlotOnFrame = True
        plotOptions.PlotPeriod = FBTime( 0, 0, 0, 1 )
        plotOptions.PlotTranslationOnRootOnly = False
        plotOptions.PreciseTimeDiscontinuities = False
        plotOptions.PlotLockedProperties = True
        plotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
        plotOptions.UseConstantKeyReducer = False
        currentCharacter.PlotAnimation (FBCharacterPlotWhere.kFBCharacterPlotOnControlRig,plotOptions )
        FBSystem().Scene.Evaluate()
    #选source
    def SetSource(self,charName): 
        print('%sSetSource%s'%(funcLogL,funcLogR))
        # 选character
        self.unSelectAll()
        foundComponents = FBComponentList()
       
        FBFindObjectsByName(charName+'_Char_New:'+'Character_Send', foundComponents, True, False)
        print(charName+'_Char_New:'+'Character_Send')
        Character = foundComponents[0]
        Character.Selected = True

        currentCharacter = FBApplication().CurrentCharacter
        #禁用并删除控制Rig

        controlRig = currentCharacter.GetCurrentControlSet()
        # 如果没有控制Rig，就创建一个新的
        if not controlRig:
            # 使用“True”参数指定的正运动学和逆运动学创建一个控制Rig
            print('创建控制器:%s_Char_New'%charName)
            bCreationResult = currentCharacter.CreateControlRig(True)
            if not bCreationResult:
                print('在PlotToControlRig中创建新的控制rig失败，请检查')
        
        # 选source
        foundComponents = FBComponentList()
        FBFindObjectsByName(str(charName+'_Char:'+'Character_Send'), foundComponents, True, False)
        if len(foundComponents):
            for i in foundComponents:
                if type(i)==FBCharacter:
                    OldCharacter = i
                    print(OldCharacter.LongName)
                    Character.InputCharacter = OldCharacter
                    Character.InputType = FBCharacterInputType.kFBCharacterInputCharacter
                    Character.ActiveInput = True
                    FBSystem().Scene.Evaluate()
                    self.PlotSkeleton() 
                                   
        else:
            print('无法找到角色体的ControlRig:%s'%charName)
            
            self.errorChar.append(charName)
               
    def unSelectAll(self):
        '''
        清理选择
        :return:
        '''
        selectedModels = pyfbsdk.FBModelList()
        pyfbsdk.FBGetSelectedModels(selectedModels, None, True)
        for select in selectedModels:
            select.Selected = False
        del (selectedModels)
    def selectModel( self,model, selected):
            """
            @selected: bool, True:select model; False: unSelect model
            hasattr  判断传入的对象是否具有给定属性
            """
            if hasattr(model, 'Selected'):
                    model.Selected = selected
    def selectBranch( self,topModel, selected):
        """
        @selected: bool, True:select model; False: unSelect model
        """
        if hasattr(topModel, 'Children'):
            for child in topModel.Children:
                self.selectBranch(child, selected)
            if hasattr(topModel, 'Selected'):
                topModel.Selected = selected

        
        
    def getFileNameAndFileDir(self):
        '''
        :use: Get FileName And FileDirPath of current MotionBuilder file
        :return: file_name, file_dir_path, file_name_list
        '''
        from pyfbsdk import FBApplication

        file_path = FBApplication().FBXFileName
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_dir_path = os.path.dirname(file_path)
        file_name_list = file_name.split('-')
        return file_name, file_dir_path, file_name_list 
    def ReplaceNamespace(self,charName):
        print('%sReplaceNamespace%s'%(funcLogL,funcLogR)) 
        CharComponents = FBComponentList()
        FBFindObjectsByName(charName+'_Char_New:*', CharComponents, True, False)
        print(charName)
        for i in CharComponents:            
            i.ProcessObjectNamespace(FBNamespaceAction.kFBReplaceNamespace,charName+'_Char_New',charName+'_Char',True)
            FBSystem().Scene.Evaluate()    
    def Main(self, control, event):
        print('%sMain%s'%(funcLogL,funcLogR))
        for i in self.CharOldList:
            print('Del:%s'%i)
            FBDeleteObjectsByName('*',i+'_Char')
            FBSystem().Scene.Evaluate()
        for i in self.CharOldList:
            self.ReplaceNamespace(i)
        for i in self.errorChar:
            print('Error:%s'%i)
                

    def getCharlist(self):
        self.CharOldList=[]
        CharComponents = FBComponentList()
        for i in CharList:
             FBFindObjectsByName(i+':Char:b_Root', CharComponents, True, False)
        for i in CharComponents:
            print (i.LongName[:-17])
            self.CharOldList.append(i.LongName[:-17])
         
    def Main1(self,control,event):
        print('%sMain1%s'%(funcLogL,funcLogR)) 
        self.saveAnimalFilePath=str(self.getFileNameAndFileDir()[1])+'\\'+str(self.getFileNameAndFileDir()[0])+'.fbx'
        print(self.saveAnimalFilePath)
        self.getCharlist()
        FBSystem().Scene.Evaluate()
        print(list(self.CharOldList))
        for charName in self.CharOldList:
            
            print('检测到的角色：%s'%charName)
            print(bodyPath[charName])
            
            self.MergeNewChar(charName,bodyPath[charName])
            self.SetSource(charName)
        for i in self.errorChar:
            self.CharOldList.remove(i) 
             
        # for i in self.CharOldList:
        #     print('Del:%s'%i)
        #     FBDeleteObjectsByName('*',i+'_Char')
        #     FBSystem().Scene.Evaluate()
        # for i in self.CharOldList:
        #     self.ReplaceNamespace(i)
        # for i in self.errorChar:
        #     print('Error:%s'%i)
                
MotionBuilderExportTool()