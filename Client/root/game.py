#add;

if app.ENABLE_REMOTE_SHOP_SYSTEM:
	import uiRemoteShop

#find;

		self.__ProcessPreservedServerCommand()

#add below;

		if app.ENABLE_REMOTE_SHOP_SYSTEM:
			self.remoteshop = None
			self.remoteshop = uiRemoteShop.RemoteShop()
			self.remoteshop.Hide()

#find;

			self.interface=None

#add below;

		if app.ENABLE_REMOTE_SHOP_SYSTEM:
			if self.remoteshop:
				self.remoteshop.Hide()
				self.remoteshop.Destroy()
				self.remoteshop = None

#find;

			"MyShopPriceList"		: self.__PrivateShop_PriceList,
		}

#add below;

		if app.ENABLE_REMOTE_SHOP_SYSTEM:
			serverCommandList["openremoteshop"] = self.OpenRemoteShop

#add to bottom;

	if app.ENABLE_REMOTE_SHOP_SYSTEM:
		def OpenRemoteShop(self):
			self.remoteshop.Show()