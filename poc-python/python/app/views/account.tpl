% rebase('base.tpl', title=title, modules=modules, client_id=client_id)
<h1 class="mt-4">{{ account.get_client_name() }}</h1>
<p>balance: {{ account.getBalance() }} €</p>
% od = "Yes" if account.overdraft else "No"
<p>overdraft: {{ od }}</p>
