% rebase('base.tpl', title=title, modules=modules, client_id=client_id)
<h1 class="mt-4">{{ client.get_full_name() }}</h1>
<p>date joint: {{ client.getDateJoint("%d/%m/%Y") }}</p>
