import uiScriptLocale,localeInfo
GOLD_COLOR	= 0xFFFEE3AE
BUTTON_ADRESS = "d:/ymir work/ui/game/myshop_deco/"

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH/2) - (190/2),
	"y" : (SCREEN_HEIGHT/2) - 100,	

	"width" : 391,
	"height" : 265+30,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 391,
			"height" : 265+30,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 391-13,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.RANGE_NPC_TITLE, 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "BlackBoard1",
					"type" : "thinboard_circle",
					"x" : 10, "y" : 36, "width" : 190-(13*2), "height" : 248,
					"children":
					(
						{
							"name" : "btn1", "type" : "button",
							"x" : 7, "y" : 9, "text": uiScriptLocale.RANGE_NPC_9001_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn2", "type" : "button",
							"x" : 7, "y" : 9+30, "text": uiScriptLocale.RANGE_NPC_9002_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn3", "type" : "button",
							"x" : 7, "y" : 9+(30*2), "text": uiScriptLocale.RANGE_NPC_9003_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn4", "type" : "button",
							"x" : 7, "y" : 9+(30*3), "text": uiScriptLocale.RANGE_NPC_9007_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn5", "type" : "button",
							"x" : 7, "y" : 9+(30*4), "text": uiScriptLocale.RANGE_NPC_20010_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn6", "type" : "button",
							"x" : 7, "y" : 9+(30*5), "text": uiScriptLocale.RANGE_NPC_9005_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn7", "type" : "button",
							"x" : 7, "y" : 9+(30*6), "text": uiScriptLocale.RANGE_NPC_20016_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
						{
							"name" : "btn8", "type" : "button",
							"x" : 7, "y" : 9+(30*7), "text": uiScriptLocale.RANGE_NPC_20022_TITLE,

							"default_image" : BUTTON_ADRESS+ "select_btn_01.sub",
							"over_image" : BUTTON_ADRESS +"select_btn_02.sub",
							"down_image" : BUTTON_ADRESS +"select_btn_03.sub",
						},
					),
				},

				{
					"name" : "BlackBoard2",
					"type" : "thinboard_circle",
					"x" : 182, "y" : 36, "width" :197, "height" : 248,
					"children":
					(
						{
							"name" : "accept_button", "type" : "button",
							"x" : 4, "y" : 9+(30*6)+28, "text": uiScriptLocale.RANGE_NPC_SHOW,
							"text_height" : 6,
							"color" : GOLD_COLOR,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},

						{
							"name" : "cancel", "type" : "button",
							"x" : 105, "y" : 9+(30*6)+28, "text": "Kapat",
							"text_height" : 6,
							"color" : GOLD_COLOR,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},
					),
				},
			),
		},
	),
}
