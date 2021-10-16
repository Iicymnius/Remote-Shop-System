import net
import ui
import app
import chrmgr
import renderTarget
import nonplayer

NPC_LIST = {
	9001 : "1",
	9002 : "4",
	9003 : "3",
	9006 : "9",
	9009 : "2",
	9005 : "7",
	20016 : "53",
	20022 : "20022"
}

class RemoteShop(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.RENDER_TARGET_INDEX = 5
		self.selectedShopVnum = 0
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE NPC EKRAN DIALOG"

	def __Initialize(self):
		self.titleBar = 0

	def Destroy(self):

		self.ClearDictionary()
		self.board = None
		self.__Initialize()
		print " -------------------------------------- DESTROY NPC EKRAN DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("NPCEkran.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.board = GetObject("board")
			
			self.btnclose = GetObject("cancel")
			self.btnclose.SAFE_SetEvent(self.cancels)
			
			self.accept_button = self.GetChild("accept_button")
			self.accept_button.SAFE_SetEvent(self.butonlar)

			GetObject("btn1").SAFE_SetEvent(self.__MenuFunction, 9001)
			GetObject("btn2").SAFE_SetEvent(self.__MenuFunction, 9002)
			GetObject("btn3").SAFE_SetEvent(self.__MenuFunction, 9003)
			GetObject("btn4").SAFE_SetEvent(self.__MenuFunction, 9006)
			GetObject("btn5").SAFE_SetEvent(self.__MenuFunction, 9009)
			GetObject("btn6").SAFE_SetEvent(self.__MenuFunction, 9005)
			GetObject("btn7").SAFE_SetEvent(self.__MenuFunction, 20016)
			GetObject("btn8").SAFE_SetEvent(self.__MenuFunction, 20022)

			self.chrRenderer =  ui.RenderTarget()
			self.chrRenderer.SetParent(self.board)
			self.chrRenderer.SetSize(190,210)
			self.chrRenderer.SetPosition(186, 39)
			self.chrRenderer.SetRenderTarget(self.RENDER_TARGET_INDEX)
			self.chrRenderer.Show()

			renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
			renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
			
		except:
			import exception
			exception.Abort("NPCEkran.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("UIScript/npcekran.py")

		self.__Load_BindObject()

		#self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def cancels(self):
		self.Hide()	

	def __MenuFunction(self, value):
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, value)
		self.selectedShopVnum = value
	
	def butonlar(self):
		net.SendChatPacket("/open_range_npc " + str(NPC_LIST[self.selectedShopVnum]))

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Show(self):
		ui.ScriptWindow.Show(self)
		self.__MenuFunction(9001)

	def Close(self):
		self.Hide()
