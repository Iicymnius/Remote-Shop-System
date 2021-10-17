//find;

ACMD(do_clear_affect);

//add below;

#ifdef ENABLE_REMOTE_SHOP_SYSTEM
ACMD(do_open_range_npc);
#endif

//find again;

			{ "do_clear_affect",		do_clear_affect,		0,	POS_DEAD,		GM_LOW_WIZARD	},

//add below;

#ifdef ENABLE_REMOTE_SHOP_SYSTEM
			{"open_range_npc",		do_open_range_npc,		0,	POS_DEAD,		GM_PLAYER	},
#endif
