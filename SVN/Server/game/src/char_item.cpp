//find;

			case 50100:

//add above;

#ifdef ENABLE_REMOTE_SHOP_SYSTEM
			case 84001://Change. Type -> ITEM_USE - SubType -> USE_SPECIAL
				ChatPacket(CHAT_TYPE_COMMAND, "openremoteshop");
				break;
#endif
