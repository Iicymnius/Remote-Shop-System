//add;

#ifdef ENABLE_REMOTE_SHOP_SYSTEM
#include "shop.h"
#include "shop_manager.h"
#endif

//find;

ACMD(do_user_horse_back)

//add above;

#ifdef ENABLE_REMOTE_SHOP_SYSTEM
ACMD(do_open_range_npc)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
		return;

	DWORD vnum = 0;
	str_to_number(vnum, arg1);

	if (ch->IsDead())
		return;

	if (ch->IsDead() || ch->GetExchange() || ch->GetMyShop() || ch->IsOpenSafebox() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("PLEASE_BEFORE_CLOSE_WINDOW_AND_USE_THIS_FUNCTION"));
		return;
	}


	LPSHOP shop = CShopManager::instance().Get(vnum);
	if (!shop) return;

	shop->AddGuest(ch, 0, false);
}
#endif
