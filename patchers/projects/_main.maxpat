{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 5,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 371.0, 190.0, 613.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 5.0, 7.0, 48.0, 20.0 ],
					"text" : "OSC In"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 0,
					"patching_rect" : [ 5.0, 29.0, 103.0, 22.0 ],
					"text" : "all_devices_in_ss"
				}

			}
 ],
		"lines" : [  ],
		"dependency_cache" : [ 			{
				"name" : "all_devices_in_ss.maxpat",
				"bootpath" : "~/Documents/Repos/dotosc/patchers/projects",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "device_in_ss.maxpat",
				"bootpath" : "~/Documents/Repos/dotosc/patchers/projects",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "imu.in.maxpat",
				"bootpath" : "~/Documents/Max 8/Library/imu/abstractions/imu.in",
				"patcherrelativepath" : "../../../../Max 8/Library/imu/abstractions/imu.in",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "imu.led.maxpat",
				"bootpath" : "~/Documents/Max 8/Library/imu/abstractions/imu.led",
				"patcherrelativepath" : "../../../../Max 8/Library/imu/abstractions/imu.led",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "imu.minmax.maxpat",
				"bootpath" : "~/Documents/Max 8/Library/imu/abstractions/imu.minmax",
				"patcherrelativepath" : "../../../../Max 8/Library/imu/abstractions/imu.minmax",
				"type" : "JSON",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
