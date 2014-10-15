		<h2 class="content-subhead" id="{{device["name"]}}">{{device["description"]}}</h2>
		<div class="pure-g">
		% for command in device["commands"]:
			% command_path = "{}/{}".format(device["name"], command["name"])
			<button class="pure-button pure-u-1-2 pure-u-md-1-3 pure-u-lg-1-4" onclick='post("{{ url('device', device=command_path) }}")'>{{command["description"] if "description" in command else command["name"]}}</button>
		% end
		</div>
		%rebase('layout.tpl', title=device["description"], devices=devices, activities=activities)