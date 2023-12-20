**MANUALE CLI**
***************

[Beehive CLI ]{.c862}

[ask ask command -eq: search equal command -a: command to search ]{.c1}

[bash-completion get bash completion script ]{.c1}

[bash-completion-envs get bash completion envs ]{.c1}

[decrypt decrypt quoted data with symmetric encryption ]{.c1}

[data: data to decrypt ]{.c1}

[key: secret key to use for encryption/decryption ]{.c1}

[encrypt encrypt data with symmetric encryption data: data to encrypt
]{.c1}

[key: secret key to use for encryption/decryption ]{.c1}

[envs list available environments -maxcolwidth: max column width.
default=50 -multichunks: split the output in chunks ]{.c1}

[-current: list only current environment ]{.c1}

[-orchestrator\_type\_name: Filter by orchestrator type name. e.g.
zabbix ]{.c1}

[gen-key generate fernet key for symmetric ]{.c1}

[encryption ]{.c1}

[gen-password generate password -length: password length ]{.c1}

[-strong: password strong ]{.c1}

[tree tree command ]{.c1}

[auth   (authorization management) ]{.c301}

[auth groups   (groups management) ]{.c2}

[auth groups add add group name: group name ]{.c1}

[-desc: group description ]{.c1}

[-expirydate: group expire date. Syntax yyyy-mm-dd ]{.c1}

[auth groups add-attrib add attribute to group id: group uuid ]{.c1}

[attrib: attribute name ]{.c1}

[value: attribute value ]{.c1}

[desc: attribute description ]{.c1}

[auth groups add-perms add permissions to group id: group uuid ]{.c1}

[perms: comma separated list of permission id ]{.c1}

[auth groups add-role add role to group id: group uuid ]{.c1}

[role: role uuid ]{.c1}

[-expirydate: group expire date. Syntax yyyy-mm-dd ]{.c1}

[auth groups add-user add user to group id: group uuid ]{.c1}

[user: user uuid ]{.c1}

[auth groups del-attrib delete attribute from group id: group uuid
]{.c1}

[attrib: attribute name ]{.c1}

[auth groups del-perms delete permissions from group id: group uuid
]{.c1}

[perms: comma separated list of permission id ]{.c1}

[auth groups del-role delete role from group id: group uuid ]{.c1}

[role: role uuid ]{.c1}

[auth groups del-user delete user from group id: group uuid ]{.c1}

[user: user uuid ]{.c1}

[auth groups delete delete group id: group uuid ]{.c1}

[auth groups get get groups -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: account uuid ]{.c1}

[-role: role id or name ]{.c1}

[-user: user id or name ]{.c1}

[-name: name filter ]{.c1}

[-desc: group desc ]{.c1}

[-email: email address ]{.c1}

[-expiry-date : expiry date. Syntax YYYY-MM-DD ]{.c1}

[-perms: rcomma separated list of permissions ]{.c1}

[auth groups get-perms get permissions of group -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group uuid]{.c1}

[auth groups update update group id: group uuid -name: group name ]{.c1}

[-desc: group description ]{.c1}

[-active: group active ]{.c1}

[auth ldap   (ldap management) ]{.c2}

[auth ldap get get user key: user key like user email -filter: search
filter ]{.c1}

[-ldap: ldap reference label ]{.c1}

[auth ldap login login user email: user email pwd: user password ]{.c1}

[-ldap: ldap reference label ]{.c1}

[auth ldap search search users value: value to search -filter: search
filter ]{.c1}

[-fields: query fields ]{.c1}

[-ldap: ldap reference label ]{.c1}

[auth oauth2-authorization-codes   (oauth2 authorization code) ]{.c2}

[auth oauth2-authorization codes delete ]{.c1}

[auth oauth2-authorization codes get ]{.c1}

[delete oauth2 authorization code id: comma separated authorization code
ids ]{.c1}

[get oauth2 authorization codes -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: authorization code id ]{.c1}

[-valid: valid ]{.c1}

[-client: client ]{.c1}

[-user: ]{.c1}

[auth oauth2-clients   (oauth2 client) ]{.c2}

[auth oauth2-clients add add oauth2 client name: client name ]{.c1}

[grant\_type: valid grant\_type: authorization\_code, implicit,
password, ]{.c1}

[client\_credentials, urn:ietf:params:oauth:grant-type:jwt-bearer ]{.c1}

[-redirect\_uri: redirect\_uri ]{.c1}

[-scopes: comma separated list of scopes ]{.c1}

[-expirydate: client expire date. Syntax yyyy-mm-dd ]{.c1}

[auth oauth2-clients delete delete oauth2 client id: client uuid ]{.c1}

[auth oauth2-clients get get oauth2 clients -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: client uuid ]{.c1}

[-role: role uuid ]{.c1}

[-group: group uuid ]{.c1}

[-name: name filter ]{.c1}

[-desc: client desc ]{.c1}

[-email: email address ]{.c1}

[-expiry-date : expiry date. Syntax YYYY-MM-DD ]{.c1}

[-perms: comma separated list of permission id ]{.c1}

[auth oauth2-scopes   (oauth2 scope) ]{.c2}

[auth oauth2-scopes add add oauth2 scope name: scope name ]{.c1}

[auth oauth2-scopes delete delete oauth2 scope id: scope uuid ]{.c1}

[auth oauth2-scopes get get oauth2 scopes -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: scope uuid ]{.c1}

[auth oauth2-tokens   (oauth2 token)]{.c2}

[auth oauth2-tokens create create oauth2 access token using
resource\_owner or client\_credentials ]{.c1}

[grant. For resource\_owner grant specify ]{.c1}

[user and pwd. For client\_credentials ]{.c1}

[specify client secret. ]{.c1}

[auth oauth2-user-sessions   (oauth2 user session) ]{.c2}

[client: client id ]{.c1}

[-user: login user -pwd: user password -secret: client secret ]{.c1}

[auth oauth2-user-sessions delete ]{.c1}

[auth oauth2-user-sessions get ]{.c1}

[delete oauth2 session id: comma separated session ids ]{.c1}

[get oauth2 sessions -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: session id ]{.c1}

[auth perms   (permission management) ]{.c2}

[auth perms add-object add object desc: user description objid:
autorization id ]{.c1}

[subsystem: subsystem ]{.c1}

[type: type ]{.c1}

[auth perms add-type add object type -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: subsystem ]{.c1}

[type: type ]{.c1}

[auth perms del-object delete object ids: comma separated list of object
id auth perms del-type delete object type id: object type uuid ]{.c1}

[auth perms get get permission -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: permission id ]{.c1}

[auth perms get-actions get object actions ]{.c1}

[auth perms get-method get method -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[rule: method url/rule ]{.c1}

[-subsystem: subsystem ]{.c1}

[auth perms get-objects get objects -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: object id ]{.c1}

[-objid: autorization id ]{.c1}

[-subsystem: subsystem ]{.c1}

[-type: type ]{.c1}

[auth perms get-types get object types -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: account uuid ]{.c1}

[-subsystem: subsystem ]{.c1}

[-type: type ]{.c1}

[auth providers   (authentication provider management) ]{.c2}

[auth providers get get authentication providers ]{.c1}

[auth roles   (roles management) ]{.c2}

[auth roles add add role name: role name -desc: role description ]{.c1}

[auth roles add-perms add permissions to role id: role uuid ]{.c1}

[perms: comma separated list of permission id]{.c1}

[auth roles del-perms delete permissions from role id: role uuid ]{.c1}

[perms: comma separated list of permission id ]{.c1}

[auth roles delete delete role id: role uuid ]{.c1}

[auth roles get get roles -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: account uuid ]{.c1}

[-user: role uuid ]{.c1}

[-group: group uuid ]{.c1}

[-names: name filter ]{.c1}

[-alias: role alias ]{.c1}

[-perms: comma separated list of permission id ]{.c1}

[auth roles get-perms get permissions of role -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: role uuid ]{.c1}

[auth roles reset-role reset permissions to full user permission ]{.c1}

[auth roles update update role id: role uuid ]{.c1}

[-name: role name ]{.c1}

[-desc: role description ]{.c1}

[auth roles use-role Use role roleid: role uuid ]{.c1}

[auth tokens   (tokens management) ]{.c2}

[auth tokens add create keyauth or oauth2 jwt token -type: can be
keyauth, oauth2. oauth2 create a token using a jwt client user: login
user ]{.c1}

[pwd: login password ]{.c1}

[-client: ouath2 client uuid ]{.c1}

[-sub: sub field for oauth2 jwt login ]{.c1}

[auth tokens delete delete token id: token uuid or all for all ]{.c1}

[auth tokens get get tokens -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: token uuid ]{.c1}

[auth tokens get-my-token return your own authentication token ]{.c1}

[auth users   (users management) ]{.c2}

[auth users add add user name: user name ]{.c1}

[-desc: user description ]{.c1}

[-storetype: can be DBUSER, LDAPUSER ]{.c1}

[-password: user password. Set only for DBUSER ]{.c1}

[-expirydate: user expire date. Syntax yyyy-mm-dd ]{.c1}

[-email: email address ]{.c1}

[auth users add-attrib add attribute to user id: user uuid ]{.c1}

[attrib: attribute name ]{.c1}

[value: attribute value ]{.c1}

[desc: attribute description ]{.c1}

[auth users add-group add group to user id: user uuid ]{.c1}

[group: group uuid ]{.c1}

[auth users add-perms add permissions to user id: user uuid ]{.c1}

[perms: comma separated list of permission id ]{.c1}

[auth users add-role add role to user id: user uuid ]{.c1}

[role: role uuid ]{.c1}

[-expirydate: user expire date. Syntax yyyy-mm-dd ]{.c1}

[auth users add-system add system user name: user name ]{.c1}

[password: user password. Set only for DBUSER ]{.c1}

[auth users del-attrib delete attribute from user id: user uuid ]{.c1}

[attrib: attribute name ]{.c1}

[auth users del-group delete group from user id: user uuid ]{.c1}

[group: group uuid ]{.c1}

[auth users del-perms delete permissions from user id: user uuid ]{.c1}

[perms: comma separated list of permission id]{.c1}

[auth users del-role delete role from user id: user uuid ]{.c1}

[role: role uuid ]{.c1}

[auth users delete delete user id: user uuid ]{.c1}

[auth users get get users -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: user uuid ]{.c1}

[-role: role uuid ]{.c1}

[-group: group uuid ]{.c1}

[-name: name filter ]{.c1}

[-desc: user desc ]{.c1}

[-email: email address ]{.c1}

[-expiry-date: expiry date. Syntax YYYY-MM-DD ]{.c1}

[-perms: comma separated list of permission id ]{.c1}

[auth users get-perms get permissions of user -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: user uuid ]{.c1}

[auth users get-secret get user secret id: user uuid ]{.c1}

[auth users update update user id: user uuid ]{.c1}

[-name: user name ]{.c1}

[-desc: user description ]{.c1}

[-active: user active ]{.c1}

[-provider: authentication provider ]{.c1}

[-password: user password. Set only for DBUSER ]{.c1}

[-expirydate: user expire date. Syntax yyyy-mm-dd ]{.c1}

[-email: email address ]{.c1}

[bu   (business service and authority management) ]{.c301}

[bu accounts   (account management) ]{.c2}

[bu accounts add add account name: account name -desc: account
description ]{.c1}

[division: division uuid ]{.c1}

[-contact: account contact ]{.c1}

[-email: account email ]{.c1}

[-email-support: account email support ]{.c1}

[-email-support-link: account email support link ]{.c1}

[-note: account note ]{.c1}

[-acronym: account acronym ]{.c1}

[-managed: if true set account as managed ]{.c1}

[bu accounts definition-add add account definitions -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: account id ]{.c1}

[definitions: comma separated list of definition ids ]{.c1}

[bu accounts definition-get get account definitions -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: account id ]{.c1}

[-plugintype: filter by definition plugin ]{.c1}

[-category: filet by category ]{.c1}

[-container: get only containers definitions ]{.c1}

[bu accounts delete delete account id: account id ]{.c1}

[-delete\_services: if true delete all child services ]{.c1}

[bu accounts get get accounts -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: account id ]{.c1}

[-objid: authorization id ]{.c1}

[-name: account name ]{.c1}

[-division-id: division uuid ]{.c1}

[-contact: account contact ]{.c1}

[-email: account email ]{.c1}

[-email-support: account email support ]{.c1}

[bu accounts manage Aminister account -size: list page size
\[default=20\] -page: list page \[default=0\]]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: the account id to manage ]{.c1}

[bu accounts operate Operate on account -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: the account id to manage ]{.c1}

[bu accounts patch refresh account id: account id ]{.c1}

[bu accounts service-active get ]{.c1}

[get account active services info id: account id ]{.c1}

[bu accounts service-del delete account services id: account id ]{.c1}

[bu accounts update update account id: account id ]{.c1}

[-desc: account description ]{.c1}

[-price\_list: account price list id ]{.c1}

[-contact: account contact ]{.c1}

[-email: account email ]{.c1}

[-email-support: account email support ]{.c1}

[-email-support-link: account email support link ]{.c1}

[-acronym: account acronym ]{.c1}

[-note: account note ]{.c1}

[bu accounts user-role-get get account user roles id: account id ]{.c1}

[bu accounts view View account -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: the account id to manage ]{.c1}

[bu accounts-auth   (account authorization) ]{.c2}

[bu accounts-auth group-add add account role to a group id: account id
]{.c1}

[role: account role ]{.c1}

[group: authorization group ]{.c1}

[bu accounts-auth group-del remove account role from a group id: account
id ]{.c1}

[role: account role ]{.c1}

[group: authorization group ]{.c1}

[bu accounts-auth group-get get account groups id: account id ]{.c1}

[bu accounts-auth role-get get account roles id: account id ]{.c1}

[bu accounts-auth user-add add account role to a user id: account id
]{.c1}

[role: account role ]{.c1}

[user: authorization user ]{.c1}

[bu accounts-auth user-del remove account role from a user id: account
id ]{.c1}

[role: account role ]{.c1}

[user: authorization user ]{.c1}

[bu accounts-auth user-get get account users id: account id ]{.c1}

[bu accounts-capabilities   (accounts capabilities) ]{.c2}

[bu accounts-capabilities add ]{.c1}

[add or update account capabilities -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: account id ]{.c1}

[capabilities: comma separated list of capability name ]{.c1}

[bu accounts-capabilities get get account capabilities id: account id
-capability: capability name ]{.c1}

[bu accounts-tags   (manage tags for account) ]{.c2}

[bu accounts-tags get get accounts -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: account id]{.c1}

[bu appeng   (appengine service management) ]{.c2}

[bu appeng info get appengine service info account: account id bu appeng
quotas get appengine service quotas account: account id ]{.c1}

[bu appeng app-instances   (appengine instances service management)
]{.c83}

[bu appeng app-instances add ]{.c1}

[bu appeng app-instances delete ]{.c1}

[bu appeng app-instances get ]{.c1}

[bu appeng app-instances list ]{.c1}

[bu appeng app-instances types ]{.c1}

[create a share name: appengine name ]{.c1}

[account: parent account id ]{.c1}

[farm-name: name of the farm ]{.c1}

[type: appengine type ]{.c1}

[subnet: appengine subnet id ]{.c1}

[sg: security group id ]{.c1}

[-key-name: ssh key name ]{.c1}

[-sharesize: share size in GB ]{.c1}

[-public: if True appengine has public ip address ]{.c1}

[-public-subnet: public subnet ]{.c1}

[delete an appengine appengine: appengine id ]{.c1}

[get appengine appengine: appengine id ]{.c1}

[list app engine -accounts: list of account id comma separated -ida:
list of appengin id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[get appengine types ]{.c1}

[bu capabilities   (capabilities management) ]{.c2}

[bu capabilities add add capability config: capability config bu
capabilities delete delete capability id: capability uuid ]{.c1}

[bu capabilities get get capabilities -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: account uuid ]{.c1}

[-objid: authorization id ]{.c1}

[bu cpaas   (compute service management) ]{.c2}

[bu cpaas availability-zones get compute service availibility zones
account: account id bu cpaas info get compute service info account:
account id bu cpaas quotas get compute service quotas account: account
id ]{.c1}

[bu cpaas compute-tags   (tags service management) ]{.c83}

[bu cpaas compute-tags add add tag to service instance account: account
id service: service instance id ]{.c1}

[tag: tag key ]{.c1}

[bu cpaas compute-tags delete ]{.c1}

[delete tag from service instance service: service instance id tag: tag
key ]{.c1}

[bu cpaas compute-tags list list resource by tags -account: account id
]{.c1}

[-services: comma separated list of service instance id ]{.c1}

[-tags: comma separated list of tag key ]{.c1}

[-types: comma separated list of service instance types ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas customizations   (customization service management) ]{.c83}

[bu cpaas customizations add ]{.c1}

[create a customization name: customization name ]{.c1}

[account: parent account id ]{.c1}

[type: customization type ]{.c1}

[instances: comma separated list of compute instance id ]{.c1}

[args: customization params. Use syntax arg1:val1,arg2:val2]{.c1}

[bu cpaas customizations delete ]{.c1}

[delete a customization customization: customization id ]{.c1}

[bu cpaas customizations get get customization customization:
customization id ]{.c1}

[bu cpaas customizations list list customizations -accounts: list of
account id comma separated -customizations: list of customization id
comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas customizations types ]{.c1}

[bu cpaas customizations update ]{.c1}

[get customizations types account: parent account id -id: customization
type id ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[update a customization customization: customization id ]{.c1}

[bu cpaas images   (image service management) ]{.c83}

[bu cpaas images add create an image name: image name account: parent
account id ]{.c1}

[desc: image description ]{.c1}

[type: image type ]{.c1}

[bu cpaas images delete delete an image image: image id ]{.c1}

[bu cpaas images get get image image: image id ]{.c1}

[bu cpaas images list list images -accounts: list of account id comma
separated -images: list of image id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas images types get image templates account: account id -id:
template id ]{.c1}

[bu cpaas keypairs   (key pair management) ]{.c83}

[bu cpaas keypairs add add new RSA key pair account: account id name:
key pair name ]{.c1}

[-type: key type ]{.c1}

[bu cpaas keypairs delete delete a key pair name: keypair name bu cpaas
keypairs get get key pair name: keypair name ]{.c1}

[bu cpaas keypairs import public-key ]{.c1}

[import public RSA key account: account id ]{.c1}

[name: key pair name ]{.c1}

[publickey: file containing public key base64 encoded ]{.c1}

[-type: key type ]{.c1}

[bu cpaas keypairs list get key pairs -accounts: list of account id
comma separated -name: list of keypair name comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas vms   (virtual machine service management)]{.c83}

[bu cpaas vms add create a virtual machine name: virtual machine name
]{.c1}

[account: parent account id ]{.c1}

[type: virtual machine type ]{.c1}

[subnet: virtual machine subnet id ]{.c1}

[image: virtual machine image id ]{.c1}

[sg: virtual machine security group id ]{.c1}

[-sshkey: virtual machine ssh key name ]{.c1}

[-pwd: virtual machine admin/root password ]{.c1}

[-main-disk: optional main disk size configuration. Use to set e default
]{.c1}

[volume type.- Use : to set a non default volume type. Ex. 5:vol.oracle
]{.c1}

[Use : to set a volume to clone ]{.c1}

[-other-disk: list of additional disk sizes comma separated. Use to set
e ]{.c1}

[default volume type.Use : to set a non default volume type. Ex. 5,10 or
]{.c1}

[5:vol.oracle,10 ]{.c1}

[-hypervisor: virtual machine hypervisor. Can be: openstack or vsphere
]{.c1}

[\[default=openstack\] ]{.c1}

[-host-group: virtual machine host group. Ex. oracle ]{.c1}

[-multi-avz: if set to False create vm to work only in the selected
]{.c1}

[availability zone \[default=True\]. Use when subnet cidr is public
]{.c1}

[-meta: virtual machine custom metadata ]{.c1}

[-skip-main-vol-size-check: Use to skip check that main volume size is
]{.c1}

[not smaller than the main volume of the template. ]{.c1}

[bu cpaas vms backup-job add ]{.c1}

[bu cpaas vms backup-job del ]{.c1}

[bu cpaas vms backup-job get ]{.c1}

[bu cpaas vms backup-job instance-add ]{.c1}

[bu cpaas vms backup-job instance-del ]{.c1}

[bu cpaas vms backup-job list ]{.c1}

[add account virtual machine backup job name: job name ]{.c1}

[account: account id ]{.c1}

[zone: job availability zone ]{.c1}

[instance: comma separated list of instance id to add ]{.c1}

[-hypervisor: job hypervisor \[openstack\] ]{.c1}

[-policy: job hypervisor \[bk-job-policy-7-7-retention\] ]{.c1}

[-desc: job description ]{.c1}

[delete account virtual machine backup job account: account id ]{.c1}

[job: job id ]{.c1}

[get account virtual machine backup job account: account id ]{.c1}

[job: job id ]{.c1}

[add virtual machine to backup job account: account id ]{.c1}

[job: job id ]{.c1}

[instance: instance id to add ]{.c1}

[delete virtual machine from backup job account: account id ]{.c1}

[job: job id ]{.c1}

[instance: instance id to add ]{.c1}

[get account virtual machine backup jobs account: account id ]{.c1}

[-hypervisor: virtual machine hypervisor. Can be: openstack or vsphere
]{.c1}

[bu cpaas vms backup-job policies ]{.c1}

[bu cpaas vms backup-job update ]{.c1}

[get account virtual machine backup job policies ]{.c1}

[update account virtual machine backup job ]{.c1}

[account: account id ]{.c1}

[account: account id ]{.c1}

[job: job id ]{.c1}

[-name: job name ]{.c1}

[-enabled: enable or disable job -policy: job policy ]{.c1}

[bu cpaas vms backup restore-add ]{.c1}

[bu cpaas vms backup restore-get ]{.c1}

[bu cpaas vms backup restore-point-add ]{.c1}

[bu cpaas vms backup restore-point-del ]{.c1}

[bu cpaas vms backup restore-point-get ]{.c1}

[restore a virtual machine from backup name: restored virtual machine
name id: id of the virtual machine to clone ]{.c1}

[restore\_point: id of restore point ]{.c1}

[get virtual machine backup restores vm: virtual machine id ]{.c1}

[restore\_point: restore point id ]{.c1}

[add backup job restore point account: account id ]{.c1}

[job: job id ]{.c1}

[name: restore point name ]{.c1}

[-desc: restore point description ]{.c1}

[-full: backup type. If true make a full backup otherwise make an ]{.c1}

[incremental backup ]{.c1}

[delete backup job restore point account: account id ]{.c1}

[job: job id ]{.c1}

[restore\_point: restore point id ]{.c1}

[get backup job restore points account: virtual machine id ]{.c1}

[-vm: virtual machine id ]{.c1}

[-job: job id ]{.c1}

[-restore\_point: restore point id ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas vms clone clone a virtual machine name: virtual machine name
id: id of the virtual machine to clone ]{.c1}

[-account: parent account id ]{.c1}

[-type: virtual machine type ]{.c1}

[-subnet: virtual machine subnet id ]{.c1}

[-sg: virtual machine security group id ]{.c1}

[-sshkey: virtual machine ssh key name ]{.c1}

[-pwd: virtual machine admin/root password]{.c1}

[-multi-avz: if set to False create vm to work only in the selected
]{.c1}

[availability zone \[default=True\]. Use when subnet cidr is public
]{.c1}

[-meta: virtual machine custom metadata ]{.c1}

[bu cpaas vms console-get get virtual machine console vm: virtual
machine id ]{.c1}

[bu cpaas vms delete delete a virtual machine vm: virtual machine id
]{.c1}

[bu cpaas vms disable monitoring ]{.c1}

[bu cpaas vms enable logging ]{.c1}

[bu cpaas vms enable monitoring ]{.c1}

[disable virtual machine monitoring vm: virtual machine id \--continues:
continue use command ]{.c1}

[enable virtual machine logging vm: virtual machine id -files: files
list ]{.c1}

[-pipeline: log collector pipeline port ]{.c1}

[\--continues: continue use command ]{.c1}

[enable virtual machine monitoring vm: virtual machine id -templates:
templates list ]{.c1}

[\--continues: continue use command ]{.c1}

[bu cpaas vms get get virtual machine vm: virtual machine id ]{.c1}

[bu cpaas vms list get virtual machine -accounts: list of account id
comma separated -ids: list of vm id comma separated ]{.c1}

[-name: vm name ]{.c1}

[-names: vm name pattern ]{.c1}

[-types: list of type comma separated ]{.c1}

[-launch\_time: launch time interval. Ex. 2021-01-30T:2021-01-31T ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-states: list of instance state comma separated ]{.c1}

[-sg: list of security group id comma separated. Ex. pending, running,
]{.c1}

[error ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-services: print instance service enabling. Ex. backup, monitoring
]{.c1}

[bu cpaas vms list-all list all the virtual machines start: vms range
lower bound ]{.c1}

[end: vms range upper bound ]{.c1}

[bu cpaas vms load import a virtual machine container: container id
where import virtual machine name: virtual machine name ]{.c1}

[vm: physical id of the virtual machine to import ]{.c1}

[image: provider image id ]{.c1}

[pwd: virtual machine password ]{.c1}

[-sshkey: virtual machine ssh key name ]{.c1}

[account: parent account id ]{.c1}

[bu cpaas vms reboot reboot a virtual machine vm: virtual machine id
]{.c1}

[-schedule: schedule definition. Pass as json file using crontab or
]{.c1}

[timedelta syntax. Ex. {\"type\": \"timedelta\", \"minutes\": 1} ]{.c1}

[bu cpaas vms refresh-state refresh virtual machine state id: virtual
machine id, uuid or name ]{.c1}

[bu cpaas vms snapshot-add add virtual machine snapshot vm: virtual
machine id ]{.c1}

[snapshot: snapshot name ]{.c1}

[bu cpaas vms snapshot-del add virtual machine snapshot vm: virtual
machine id ]{.c1}

[snapshot: snapshot id ]{.c1}

[bu cpaas vms snapshot-get list virtual machine snapshots vm: virtual
machine id ]{.c1}

[bu cpaas vms snapshot revert ]{.c1}

[revert virtual machine snapshot vm: virtual machine id snapshot:
snapshot id ]{.c1}

[bu cpaas vms start start a virtual machine vm: virtual machine id
]{.c1}

[-schedule: schedule definition. Pass as json file using crontab or
]{.c1}

[timedelta syntax. Ex. {\"type\": \"timedelta\", \"minutes\": 1} ]{.c1}

[bu cpaas vms stop stop a virtual machine vm: virtual machine id ]{.c1}

[-schedule: schedule definition. Pass as json file using crontab or
]{.c1}

[timedelta syntax. Ex. {\"type\": \"timedelta\", \"minutes\": 1} ]{.c1}

[bu cpaas vms types get virtual machine types account: parent account id
]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas vms update update a virtual machine vm: virtual machine id
]{.c1}

[-type: virtual machine type ]{.c1}

[-sg\_add: virtual machine security group id to add ]{.c1}

[-sg\_del: virtual machine security group id to remove ]{.c1}

[bu cpaas vms user-add add virtual machine user vm: virtual machine id
]{.c1}

[name: user name ]{.c1}

[pwd: user password ]{.c1}

[key: ssh key id ]{.c1}

[bu cpaas vms user-del delete virtual machine user vm: virtual machine
id ]{.c1}

[name: user name ]{.c1}

[bu cpaas vms user- set virtual machine user password vm: virtual
machine id]{.c1}

[password-set name: user name ]{.c1}

[pwd: user password ]{.c1}

[bu cpaas volumes   (volume service management) ]{.c83}

[bu cpaas volumes add create a volume name: volume name ]{.c1}

[account: parent account id ]{.c1}

[availability\_zone: volume availability\_zone ]{.c1}

[type: volume type ]{.c1}

[size: volume sise ]{.c1}

[-iops: volume iops ]{.c1}

[-snapshot: volume snapshot ]{.c1}

[-hypervisor: volume hypervisor. Can be: openstack or vsphere ]{.c1}

[\[default=openstack\] ]{.c1}

[bu cpaas volumes attach attach a volume to an instance volume: volume
id ]{.c1}

[instance: instance id ]{.c1}

[bu cpaas volumes delete delete a volume volume: volume id ]{.c1}

[bu cpaas volumes detach detach a volume to an instance volume: volume
id ]{.c1}

[instance: instance id ]{.c1}

[bu cpaas volumes get get volume volume: volume id ]{.c1}

[bu cpaas volumes list list volumes -accounts: list of account id comma
separated -volumes: list of volume id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu cpaas volumes load load volumes from resources account: account id
]{.c1}

[volume\_name: name ]{.c1}

[volume\_resource\_id: resource volume id ]{.c1}

[bu cpaas volumes types get volumes types account: parent account id
]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu dbaas   (database service management) ]{.c2}

[bu dbaas info get database service info account: account id ]{.c1}

[bu dbaas quotas get database service quotas account: account id ]{.c1}

[bu dbaas db-instances   (database instance service management) ]{.c83}

[bu dbaas db-instances add mysql ]{.c1}

[bu dbaas db-instances add oracle ]{.c1}

[bu dbaas db-instances add postgresql ]{.c1}

[create mysql db instance name: db instance name ]{.c1}

[account: parent account id ]{.c1}

[type: db instance type ]{.c1}

[subnet: db instance subnet id ]{.c1}

[sg: db instance security group id ]{.c1}

[version: database engine version ]{.c1}

[-pwd: db root password ]{.c1}

[-storage: data storage capacity in GB ]{.c1}

[-keyname: ssh key name ]{.c1}

[create oracle db instance name: db instance name ]{.c1}

[account: parent account id ]{.c1}

[type: db instance type ]{.c1}

[subnet: db instance subnet id ]{.c1}

[sg: db instance security group id ]{.c1}

[version: database engine version ]{.c1}

[-pwd: db root password ]{.c1}

[-keyname: ssh key name ]{.c1}

[-dbname: db name \[default: ORCL0\] ]{.c1}

[-lsnport: listener port \[default: 1521\] ]{.c1}

[-archmode: archivelog mode Y/N \[default: Y\] ]{.c1}

[-partopt: partitioning option Y/N \[default: Y\] ]{.c1}

[-charset: character set \[default: WE8ISO8859P1\] ]{.c1}

[-natcharset: national charset \[default: AL16UTF16\] ]{.c1}

[-dbfdisksize: datafiles disk size in GB \[default: 30\] ]{.c1}

[-recodisksize: recovery disk size in GB \[default: 20\] ]{.c1}

[create postgresql db instance name: db instance name ]{.c1}

[account: parent account id ]{.c1}

[type: db instance type ]{.c1}

[subnet: db instance subnet id ]{.c1}

[sg: db instance security group id ]{.c1}

[version: database engine version ]{.c1}

[-storage: amount of storage \[GB\] to allocate for the DB instance
]{.c1}

[-pwd: db root password]{.c1}

[bu dbaas db-instances add sqlserver ]{.c1}

[bu dbaas db-instances database-add ]{.c1}

[bu dbaas db-instances database-del ]{.c1}

[bu dbaas db-instances database-get ]{.c1}

[bu dbaas db-instances delete ]{.c1}

[bu dbaas db-instances disable-monitoring ]{.c1}

[bu dbaas db-instances enable-logging ]{.c1}

[bu dbaas db-instances enable-monitoring ]{.c1}

[bu dbaas db-instances engines ]{.c1}

[-keyname: ssh key name ]{.c1}

[-postgis: spatial database extension ]{.c1}

[create sqlserver db instance name: db instance name account: parent
account id ]{.c1}

[type: db instance type ]{.c1}

[subnet: db instance subnet id ]{.c1}

[sg: db instance security group id ]{.c1}

[version: database engine version ]{.c1}

[-pwd: db root password ]{.c1}

[-storage: data storage capacity in GB ]{.c1}

[-keyname: ssh key name ]{.c1}

[create a db instance database/schema instance: db instance id name:
database name ]{.c1}

[charset: database charset ]{.c1}

[delete a db instance database/schema instance: db instance id name:
database name ]{.c1}

[get db instance databases/schemas instance: db instance id delete a db
instance database: db instance id disable db instance monitoring
instance: db instance id ]{.c1}

[enable db instance logging instance: virtual machine id -files: files
list ]{.c1}

[-pipeline: log collector pipeline port ]{.c1}

[enable db instance monitoring instance: db instance id -templates:
templates list ]{.c1}

[get database instance engines account: parent account id ]{.c1}

[bu dbaas db-instances get get database instance id: database id ]{.c1}

[bu dbaas db-instances list get database instances -accounts: list of
account id comma separated -ids: list of db instance id comma separated
]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu dbaas db-instances reboot ]{.c1}

[reboot a db instance database: db instance id ]{.c1}

[bu dbaas db-instances start start a db instance database: db instance
id bu dbaas db-instances stop stop a db instance database: db instance
id ]{.c1}

[bu dbaas db-instances types get database instance types account: parent
account id -page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu dbaas db-instances update ]{.c1}

[bu dbaas db-instances user add ]{.c1}

[bu dbaas db-instances user del ]{.c1}

[bu dbaas db-instances user get ]{.c1}

[bu dbaas db-instances user password-set ]{.c1}

[bu dbaas db-instances user priv-grant ]{.c1}

[bu dbaas db-instances user priv-revoke ]{.c1}

[update a db instance instance: db instance id ]{.c1}

[-dbi\_class: db instance class to set up ]{.c1}

[-sg\_add: db instance security group id to add ]{.c1}

[-sg\_del: db instance security group id to remove ]{.c1}

[-resize: new amount of storage (in GiB) to allocate for the db instance
]{.c1}

[-extensions\_add: db extensions to install, e.g. ]{.c1}

[name1:type1,name2:type2,\... where type can be plugin or component
]{.c1}

[create a db instance user instance: db instance id ]{.c1}

[name: user name ]{.c1}

[pwd: user password ]{.c1}

[delete a db instance user instance: db instance id ]{.c1}

[name: user name ]{.c1}

[-force: force deletion ]{.c1}

[get db instance users instance: db instance id ]{.c1}

[change db instance user password instance: db instance id ]{.c1}

[name: user name ]{.c1}

[pwd: user password ]{.c1}

[grant db instance user privileges instance: db instance id ]{.c1}

[name: user name ]{.c1}

[db\_name: database name. For postgres use db1 to select a database e
]{.c1}

[db1.schema1 to select schema schema1 in database db1 ]{.c1}

[privileges: privileges admitted: mysql - ]{.c1}

[SELECT,INSERT,DELETE,UPDATE,ALL, postgres db - CONNECT, ]{.c1}

[postgres schema - USAGE,CREATE,ALL ]{.c1}

[revoke db instance user privileges instance: db instance id ]{.c1}

[name: user name ]{.c1}

[db\_name: database name. For postgres use db1 to select a database e
]{.c1}

[db1.schema1 to select schema schema1 in database db1 ]{.c1}

[privileges: privileges admitted: mysql -]{.c1}

[SELECT,INSERT,DELETE,UPDATE,ALL, postgres db - CONNECT, ]{.c1}

[postgres schema - USAGE,CREATE,ALL ]{.c1}

[bu divs   (division management) ]{.c2}

[bu divs add add division name: division name ]{.c1}

[-desc: division description ]{.c1}

[organization: organization uuid ]{.c1}

[-contact: division contact ]{.c1}

[-email: division email ]{.c1}

[-postaladdress: division postaladdress ]{.c1}

[-price\_list: division price list id ]{.c1}

[bu divs delete delete division id: division uuid ]{.c1}

[bu divs get get divisions -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: division uuid ]{.c1}

[-objid: authorization id ]{.c1}

[-name: division name ]{.c1}

[-organization-id: organization uuid ]{.c1}

[-contact: division contact ]{.c1}

[-email: division email ]{.c1}

[-postaladdress: division legalemail ]{.c1}

[bu divs patch refresh division id: division uuid ]{.c1}

[bu divs update update division name: division name ]{.c1}

[-desc: division description ]{.c1}

[organization: organization uuid ]{.c1}

[-contact: division contact ]{.c1}

[-email: division email ]{.c1}

[-postaladdress: division postaladdress ]{.c1}

[-price\_list\_id: division price list id ]{.c1}

[bu divs-auth   (division authorization) ]{.c2}

[bu divs-auth group-add add division role to a group id: division uuid
]{.c1}

[role: division role ]{.c1}

[group: authorization group ]{.c1}

[bu divs-auth group-del remove division role from a group id: division
uuid ]{.c1}

[role: division role ]{.c1}

[group: authorization group ]{.c1}

[bu divs-auth group-get get division groups id: division uuid ]{.c1}

[bu divs-auth role-get get division roles id: division uuid ]{.c1}

[bu divs-auth user-add add division role to a user id: division uuid
]{.c1}

[role: division role ]{.c1}

[user: authorization user ]{.c1}

[bu divs-auth user-del remove division role from a user id: division
uuid ]{.c1}

[role: division role ]{.c1}

[user: authorization user ]{.c1}

[bu divs-auth user-get get division users id: division uuid ]{.c1}

[bu logaas   (logging service management) ]{.c2}

[bu logaas info get logging service info account: account id ]{.c1}

[bu logaas quotas get logging service quotas account: account id ]{.c1}

[bu logaas instances   (logging instance service management) ]{.c83}

[bu logaas instances add create a logging instance account: parent
account id ]{.c1}

[instance: instance ]{.c1}

[-definition: definition ]{.c1}

[-norescreate: don\'t create physical resource of the folder ]{.c1}

[bu logaas instances configs get logging module configs account: parent
account id ]{.c1}

[bu logaas instances delete delete a logging instance instance\_id:
logging instance id bu logaas instances disable- disable logging module
instance\_id: logging instance id]{.c1}

[module conf: module configuration ]{.c1}

[bu logaas instances enable module ]{.c1}

[enable logging module instance\_id: logging instance id conf: module
configuration ]{.c1}

[bu logaas instances get get logging instance id: logging instance id
]{.c1}

[bu logaas instances list list logging instances -accounts: list of
account id comma separated -name: list of logging instances id comma
separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu logaas spaces   (logging space service management) ]{.c83}

[bu logaas spaces add create a logging space account: parent account id
-name: space name ]{.c1}

[-definition: service definition of the space ]{.c1}

[-norescreate: don\'t create physical resource of the folder ]{.c1}

[bu logaas spaces delete delete a logging space logging\_space\_id:
logging space id bu logaas spaces get get logging space id: space id
]{.c1}

[bu logaas spaces list list logging spaces -accounts: list of account id
comma separated -name: list of logging instances id comma separated
]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu logaas spaces sync-users synchronize users of logging space
logging\_space\_id: logging space id ]{.c1}

[bu maas   (monitoring service management) ]{.c2}

[bu maas availability-zones get monitoring service availibility zones
account: account id ]{.c1}

[bu maas info get monitoring service info account: account id ]{.c1}

[bu maas quotas get monitoring service quotas account: account id ]{.c1}

[bu maas alerts   (monitoring alert service management) ]{.c83}

[bu maas alerts add create a monitoring alert account: parent account id
zone: availability zone ]{.c1}

[-name: alert name ]{.c1}

[-definition: service definition of the alert ]{.c1}

[-norescreate: don\'t create physical resource of the alert ]{.c1}

[bu maas alerts delete delete a monitoring alert monitoring\_alert\_id:
monitoring alert id bu maas alerts get get monitoring alert id: alert id
]{.c1}

[bu maas alerts list list monitoring alerts -accounts: list of account
id comma separated -name: list of monitoring instances id comma
separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu maas alerts user severities ]{.c1}

[get monitoring alert user severities ]{.c1}

[bu maas alerts user-update update user of monitoring alert id: alert id
]{.c1}

[users\_email: users email that will receive alerts - comma separated
]{.c1}

[severity: list of alert severity - comma separated ]{.c1}

[bu maas folders   (monitoring folder service management) ]{.c83}

[bu maas folders add create a monitoring folder account: parent account
id ]{.c1}

[-name: folder name ]{.c1}

[-definition: service definition of the folder ]{.c1}

[-norescreate: don\'t create physical resource of the folder ]{.c1}

[bu maas folders dashboards get monitoring folder configs account:
parent account id ]{.c1}

[bu maas folders delete delete a monitoring folder
monitoring\_folder\_id: monitoring folder id ]{.c1}

[bu maas folders enable dashboard ]{.c1}

[enable monitoring dashboard folders\_id: folders id conf: dashboard
configuration ]{.c1}

[bu maas folders get get monitoring folder id: folder id]{.c1}

[bu maas folders list list monitoring folders -accounts: list of account
id comma separated -name: list of monitoring instances id comma
separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu maas folders sync-users synchronize users of monitoring folder
monitoring\_folder\_id: monitoring folder id ]{.c1}[bu maas
monitor-instances   (monitoring instance service management) ]{.c83}

[bu maas monitor-instances add ]{.c1}

[bu maas monitor-instances delete ]{.c1}

[bu maas monitor-instances get ]{.c1}

[bu maas monitor-instances list ]{.c1}

[create a monitoring instance account: parent account id ]{.c1}

[instance: instance ]{.c1}

[-definition: definition ]{.c1}

[-norescreate: don\'t create physical resource of the folder ]{.c1}

[delete a monitoring instance instance\_id: monitoring instance id get
monitoring instance id: monitoring instance id ]{.c1}

[list monitoring instances -accounts: list of account id comma separated
-name: list of monitoring instances id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas   (network service management) ]{.c2}

[bu netaas availability-zones get network service availibility zones
account: account id bu netaas info get network service info account:
account id bu netaas quotas get network service quotas account: account
id ]{.c1}

[bu netaas health-monitors   (health monitor service management) ]{.c83}

[bu netaas health-monitors add ]{.c1}

[bu netaas health-monitors delete ]{.c1}

[bu netaas health-monitors get ]{.c1}

[bu netaas health-monitors list ]{.c1}

[bu netaas health-monitors templates ]{.c1}

[bu netaas health-monitors update ]{.c1}

[create health monitor name: monitor name ]{.c1}

[account: parent account id ]{.c1}

[protocol: protocol used to perform targets health check: \[\'http\',
\'https\', ]{.c1}

[\'tcp\', \'imcp\', \'udp\'\] ]{.c1}

[-desc: health monitor description ]{.c1}

[-interval: interval in seconds in which a server is to be tested ]{.c1}

[-timeout: maximum time in seconds in which a response from the ]{.c1}

[server must be received ]{.c1}

[-max\_retries: maximum number of times the server is tested before it
]{.c1}

[is declared down ]{.c1}

[-method: method to send the health check request to the server:
\[\'get\', ]{.c1}

[\'post\', \'options\'\] ]{.c1}

[-url: URL to GET or POST ]{.c1}

[-expected: expected string ]{.c1}

[delete health monitors ids: comma separated health monitor ids ]{.c1}

[get health monitor id: health monitor uuid or name ]{.c1}

[list health monitors -accounts: list of comma separated account ids
-ids: list of comma separated health monitor ids ]{.c1}

[-tags: list of comma separated tags ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[get health monitor templates account: account id ]{.c1}

[-id: template id ]{.c1}

[update health monitor id: health monitor id ]{.c1}

[-interval: interval in seconds in which a server is to be tested ]{.c1}

[-timeout: maximum time in seconds in which a response from the ]{.c1}

[server must be received ]{.c1}

[-max\_retries: maximum number of times the server is tested before it
]{.c1}

[is declared down ]{.c1}

[-method: method to send the health check request to the server:
\[\'get\', ]{.c1}

[\'post\', \'options\'\] ]{.c1}

[-url: URL to GET or POST ]{.c1}

[-expected: expected string ]{.c1}

[bu netaas internet-gateways   (gateways service management) ]{.c83}

[bu netaas internet gateways add ]{.c1}

[create a gateway account: parent account id -template: template
id]{.c1}

[bu netaas internet gateways bastion-add ]{.c1}

[bu netaas internet gateways bastion-del ]{.c1}

[bu netaas internet gateways bastion-get ]{.c1}

[bu netaas internet gateways delete ]{.c1}

[bu netaas internet gateways get ]{.c1}

[bu netaas internet gateways list ]{.c1}

[bu netaas internet gateways patch ]{.c1}

[bu netaas internet gateways templates ]{.c1}

[bu netaas internet gateways vpc-attach ]{.c1}

[bu netaas internet gateways vpc-detach ]{.c1}

[create a gateway bastion gateway: gateway id ]{.c1}

[delete a gateway bastion gateway: gateway id ]{.c1}

[get gateway bastion gateway: gateway id ]{.c1}

[delete a gateway gateway: gateway id ]{.c1}

[get gateway gateway: gateway id ]{.c1}

[get gateways -accounts: list of account id comma separated -ids: list
of gateway id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[patch a gateway gateway: gateway id ]{.c1}

[get gateway templates account: account id ]{.c1}

[-id: template id ]{.c1}

[attach vpc from gateway gateway: gateway id ]{.c1}

[vpc: vpc id ]{.c1}

[detach vpc from gateway gateway: gateway id ]{.c1}

[vpc: vpc id ]{.c1}

[bu netaas listeners   (listener service management) ]{.c83}

[bu netaas listeners add create listener name: listener name ]{.c1}

[account: parent account id ]{.c1}

[traffic\_type: incoming traffic profile; one of: \[\'tcp\', \'http\',
\'ssl ]{.c1}

[passthrough\', \'https-offloading\', \'https-end-to-end\'\] ]{.c1}

[-desc: listener description ]{.c1}

[-persistence: persistence type: \[\'sourceip\', \'cookie\',
\'ssl-sessionid\'\] ]{.c1}

[-cookie\_name: cookie name ]{.c1}

[-cookie\_mode: cookie mode: \[\'insert\', \'prefix\', \'app-session\'\]
]{.c1}

[-expire: expire time in seconds ]{.c1}

[-client\_cert\_path: client certificate path ]{.c1}

[-server\_cert\_path: server certificate path ]{.c1}

[-client\_cipher: cipher suite used by client; one of: \[\'DEFAULT\',
]{.c1}

[\'ECDHE-RSA-AES128-GCM-SHA256\', \'ECDHE-RSA-AES256-GCM ]{.c1}

[SHA384\', \'ECDHE-RSA-AES256-SHA\', \'ECDHE-ECDSA-AES256-SHA\', ]{.c1}

[\'ECDH-ECDSA-AES256-SHA\', \'ECDH-RSA-AES256-SHA\', \'AES256- ]{.c1}

[SHA\', \'AES128-SHA\', \'DES-CBC3-SHA\'\] ]{.c1}

[-server\_cipher: cipher suite used by server; one of: \[\'DEFAULT\',
]{.c1}

[\'ECDHE-RSA-AES128-GCM-SHA256\', \'ECDHE-RSA-AES256-GCM ]{.c1}

[SHA384\', \'ECDHE-RSA-AES256-SHA\', \'ECDHE-ECDSA-AES256-SHA\', ]{.c1}

[\'ECDH-ECDSA-AES256-SHA\', \'ECDH-RSA-AES256-SHA\', \'AES256- ]{.c1}

[SHA\', \'AES128-SHA\', \'DES-CBC3-SHA\'\] ]{.c1}

[-insert\_x\_forwarded\_for: insert X-Forwarded-For HTTP header ]{.c1}

[-redirect\_to: url to redirect client requests ]{.c1}

[bu netaas listeners delete delete listeners ids: comma separated
listener ids ]{.c1}

[bu netaas listeners get get listener id: listener uuid or name ]{.c1}

[bu netaas listeners list list listeners -accounts: list of comma
separated account ids -ids: list of comma separated listener ids ]{.c1}

[-tags: list of comma separated tags ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas listeners templates ]{.c1}

[get listener templates account: account id -id: template id ]{.c1}

[bu netaas listeners update update listener id: listener id ]{.c1}

[-desc: listener description ]{.c1}

[-persistence: persistence type: \[\'sourceip\', \'cookie\',
\'ssl-sessionid\'\] ]{.c1}

[-cookie\_name: cookie name ]{.c1}

[-cookie\_mode: cookie mode: \[\'insert\', \'prefix\', \'app-session\'\]
]{.c1}

[-expire: expire time in seconds ]{.c1}

[-insert\_x\_forwarded\_for: insert X-Forwarded-For HTTP header,
\[\'True\', ]{.c1}

[\'False\'\] ]{.c1}

[-redirect\_to: url to redirect client requests ]{.c1}

[bu netaas load-balancers   (load balancer service management) ]{.c83}

[bu netaas load-balancers add ]{.c1}

[create load balancer name: load balancer name ]{.c1}

[account: parent account id ]{.c1}

[template: load balancer service definition ]{.c1}

[protocol: protocol for connections to load balancer: \[\'http\',
\'https\'\] ]{.c1}

[port: port number]{.c1}

[bu netaas load-balancers delete ]{.c1}

[bu netaas load-balancers delete-predefined-service ]{.c1}

[bu netaas load-balancers get ]{.c1}

[bu netaas load-balancers list ]{.c1}

[bu netaas load-balancers start ]{.c1}

[bu netaas load-balancers stop ]{.c1}

[bu netaas load-balancers templates ]{.c1}

[bu netaas load-balancers update ]{.c1}

[listener: listener id ]{.c1}

[target\_group: target group id ]{.c1}

[-desc: load balancer description ]{.c1}

[-static\_ip: load balancer frontend ip address ]{.c1}

[-max\_conn: maximum concurrent connections ]{.c1}

[-max\_conn\_rate: maximum connections per second ]{.c1}

[-deploy\_env: project deployment environment: \[\'prod\', \'preprod\',
]{.c1}

[\'stage\', \'test\'\] ]{.c1}

[delete load balancer id: load balancer id ]{.c1}

[delete load balancer generic services account: account id ]{.c1}

[get load balancer id: load balancer uuid or name ]{.c1}

[list load balancers -accounts: list of comma separated account ids
-ids: list of comma separated load balancer ids ]{.c1}

[-tags: list of comma separated tags ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[enable load balancer id: load balancer id ]{.c1}

[disable load balancer id: load balancer id ]{.c1}

[get load balancer templates account: account id ]{.c1}

[-id: template id ]{.c1}

[update load balancer id: load balancer id ]{.c1}

[-desc: load balancer description ]{.c1}

[-protocol: protocol for connections to load balancer: \[\'http\',
\'https\'\] ]{.c1}

[-port: port number ]{.c1}

[-max\_conn: maximum concurrent connections ]{.c1}

[-max\_conn\_rate: maximum connections per second ]{.c1}

[bu netaas securitygroups   (security groups service management) ]{.c83}

[bu netaas securitygroups add ]{.c1}

[bu netaas securitygroups add-rule ]{.c1}

[bu netaas securitygroups del-rule ]{.c1}

[bu netaas securitygroups delete ]{.c1}

[bu netaas securitygroups get ]{.c1}

[bu netaas securitygroups list ]{.c1}

[bu netaas securitygroups patch ]{.c1}

[bu netaas securitygroups templates ]{.c1}

[create a security group name: security group name ]{.c1}

[vpc: parent vpc ]{.c1}

[-template: template id ]{.c1}

[add a security group rule type: egress or ingress. For egress rule the
destination. For ingress rule specify the source ]{.c1}

[securitygroup: securitygroup id ]{.c1}

[-proto: protocol. can be tcp, udp, icmp or -1 for all ]{.c1}

[-port: can be an integer between 0 and 65535 or a range with start
]{.c1}

[and end in the same interval. Range format is -. Use -1 for all ports.
]{.c1}

[Set subprotocol if proto is icmp (8 for ping) ]{.c1}

[-dest: rule destination. Syntax :. Destination type can be SG, CIDR.
For ]{.c1}

[SG value must be . For CIDR value should like 10.102.167.0/24. ]{.c1}

[-source: rule source. Syntax :. Source type can be SG, CIDR. For SG
]{.c1}

[value must be . For CIDR value should like 10.102.167.0/24. ]{.c1}

[delete a security group rule type: egress or ingress. For egress rule
the destination. For ingress rule specify the source ]{.c1}

[securitygroup: securitygroup id ]{.c1}

[-proto: protocol. can be tcp, udp, icmp or -1 for all ]{.c1}

[-port: can be an integer between 0 and 65535 or a range with start
]{.c1}

[and end in the same interval. Range format is -. Use -1 for all ports.
]{.c1}

[Set subprotocol if proto is icmp (8 for ping) ]{.c1}

[-dest: rule destination. Syntax :. Destination type can be SG, CIDR.
For ]{.c1}

[SG value must be . For CIDR value should like 10.102.167.0/24. ]{.c1}

[-source: rule source. Syntax :. Source type can be SG, CIDR. For SG
]{.c1}

[value must be . For CIDR value should like 10.102.167.0/24. ]{.c1}

[delete a security group securitygroup: securitygroup id ]{.c1}

[get security group with rules securitygroup: securitygroup id ]{.c1}

[get security groups -accounts: list of account id comma separated -ids:
list of security group id comma separated ]{.c1}

[-vpcs: list of vpc id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[patch a security group securitygroup: securitygroup id ]{.c1}

[get security group templates account: account id ]{.c1}

[-id: template id ]{.c1}

[bu netaas sshgw   (ssh gateway service management)]{.c83}

[bu netaas sshgw conf activate ]{.c1}

[activate ssh gw configuration id: ssh gateway conf id port: destination
port ]{.c1}

[bu netaas sshgw conf-add add ssh gateway configuration name:
configuration name ]{.c1}

[gw\_type: ssh gateway type (gw\_dbaas,gw\_cpaas) ]{.c1}

[-desc: configuration description ]{.c1}

[dest\_uuid: destination service instance uuid ]{.c1}

[-allowed\_ports: comma separated list of ranges (start-end) or single
]{.c1}

[ports. e.g. 8000-9000,22 ]{.c1}

[-forbidden\_ports: comma separated list of ranges (start-end) or single
]{.c1}

[ports. e.g. 8000-9000,22 ]{.c1}

[bu netaas sshgw conf-delete delete a ssh gateway configuration id: ssh
gateway conf id ]{.c1}

[bu netaas sshgw conf-get get ssh gateway configuration id: ssh gateway
configuration id ]{.c1}

[bu netaas sshgw conf-list get ssh gateway configurations -accounts:
list of account id comma separated -ids: list of ssh gateway
configurations id comma separated ]{.c1}

[-names: list of ssh gateway configurations names comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas subnets   (vpc subnet service management) ]{.c83}

[bu netaas subnets add add virtual private cloud subnet name: subnet
name ]{.c1}

[vpc: vpc id ]{.c1}

[cidr\_block: subnet cidr block ]{.c1}

[zone: availability zone ]{.c1}

[-template: subnet template ]{.c1}

[bu netaas subnets delete delete a subnet subnet: subnet id ]{.c1}

[bu netaas subnets list get vpc subnets -accounts: list of account id
comma separated -ids: list of subnet id comma separated ]{.c1}

[-vpcs: list of vpc id comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas subnets templates ]{.c1}

[get vpc templates account: account id -id: template id ]{.c1}

[bu netaas target-groups   (target group service management) ]{.c83}

[bu netaas target-groups add ]{.c1}

[bu netaas target-groups delete ]{.c1}

[create empty target group name: target group name ]{.c1}

[account: parent account id ]{.c1}

[balancing\_algorithm: algorithm used to load balance targets: \[\'round
]{.c1}

[robin\', \'ip-hash\', \'leastconn\', \'uri\'\] ]{.c1}

[target\_type: target type: \[\'vm\', \'container\'\] ]{.c1}

[-desc: target group description ]{.c1}

[-health\_monitor: id of the custom monitor to perform health checks on
]{.c1}

[targets ]{.c1}

[-transparent: whether client IP addresses are visible to the backend
]{.c1}

[servers, \[True, False\] ]{.c1}

[delete target groups ids: comma separated target group ids ]{.c1}

[bu netaas target-groups get get target group id: target group uuid or
name ]{.c1}

[bu netaas target-groups health-monitor-deregister ]{.c1}

[deregister health monitor from target group ]{.c1}

[id: target group id ]{.c1}

[bu netaas target-groups health-monitor-register ]{.c1}

[register health monitor with target group id: target group id monitor:
health monitor id ]{.c1}

[bu netaas target-groups list list target groups -accounts: list of
comma separated account ids -ids: list of comma separated target group
ids ]{.c1}

[-tags: list of comma separated tags ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas target-groups targets-deregister ]{.c1}

[bu netaas target-groups targets-register ]{.c1}

[bu netaas target-groups templates ]{.c1}

[deregister targets from target group id: target group id ]{.c1}

[targets: comma separated list of target ids ]{.c1}

[register targets with target group id: target group id ]{.c1}

[targets: comma separated list of couples : or triplets :: ]{.c1}

[get target group templates account: account id ]{.c1}

[-id: template id]{.c1}

[bu netaas target-groups update ]{.c1}

[update target group id: target group id ]{.c1}

[-desc: target group description ]{.c1}

[-balancing\_algorithm: algorithm used to load balance targets:
\[\'round ]{.c1}

[robin\', \'ip-hash\', \'leastconn\', \'uri\'\] ]{.c1}

[-transparent: whether client IP addresses are visible to the backend
]{.c1}

[servers, \[True, False\] ]{.c1}

[bu netaas vpcs   (virtual private cloud network service management)
]{.c83}

[bu netaas vpcs add add virtual private cloud name: vpc name ]{.c1}

[account: account id ]{.c1}

[cidr\_block: vpc cidr block ]{.c1}

[-template: vpc template ]{.c1}

[-tenancy: allowed tenancy of instances launched into the VPC. Use
]{.c1}

[default for shared vpc. Use dedicated for private vpc. default is
]{.c1}

[dedicated ]{.c1}

[bu netaas vpcs delete delete a vpc vpc: vpc id ]{.c1}

[bu netaas vpcs list get private cloud networks -accounts: list of
account id comma separated -ids: list of private cloud network id comma
separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu netaas vpcs templates get vpc templates account: account id ]{.c1}

[-id: template id ]{.c1}

[bu orgs   (organization management) ]{.c2}

[bu orgs active-services get organization active services info id:
organization uuid or name ]{.c1}

[bu orgs add add organization name: organization name ]{.c1}

[-desc: organization description ]{.c1}

[-attrib: organization attributes ]{.c1}

[orgtype: organization type ]{.c1}

[-hasvat: organization hasvat ]{.c1}

[-ext-anag-id: organization ext\_anag\_id ]{.c1}

[-partner: organization partner ]{.c1}

[-referent: organization referent ]{.c1}

[-email: organization email ]{.c1}

[-legalemail: organization legalemail ]{.c1}

[-postaladdress: organization legalemail ]{.c1}

[bu orgs delete delete organization id: organization uuid or name ]{.c1}

[bu orgs get get organizations -size: list page size \[default=20\]
]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: organization uuid ]{.c1}

[-objid: authorization id ]{.c1}

[-name: organization name ]{.c1}

[-org-type: organization type ]{.c1}

[-ext-anag-id: organization ext\_anag\_id ]{.c1}

[-attributes: organization attributes ]{.c1}

[-hasvat: organization hasvat ]{.c1}

[-partner: organization partner ]{.c1}

[-referent: organization referent ]{.c1}

[-email: organization email ]{.c1}

[-legalemail: organization legalemail ]{.c1}

[-postaladdress: organization legalemail ]{.c1}

[bu orgs refresh refresh organization id: organization uuid or name
]{.c1}

[bu orgs update update organization name: organization name ]{.c1}

[-desc: organization description ]{.c1}

[-attrib: organization attributes ]{.c1}

[org-type: organization type ]{.c1}

[-hasvat: organization hasvat ]{.c1}

[-ext-anag-id: organization ext\_anag\_id ]{.c1}

[-partner: organization partner ]{.c1}

[-referent: organization referent ]{.c1}

[-email: organization email ]{.c1}

[-legalemail: organization legalemail ]{.c1}

[-postaladdress: organization legalemail ]{.c1}

[bu orgs-auth   (organization authorization)]{.c2}

[bu orgs-auth group-add add organization role to a group id:
organization uuid role: organization role ]{.c1}

[group: authorization group ]{.c1}

[bu orgs-auth group-del remove organization role from a group id:
organization uuid role: organization role ]{.c1}

[group: authorization group ]{.c1}

[bu orgs-auth group-get get organization groups id: organization uuid bu
orgs-auth role-get get organization roles id: organization uuid ]{.c1}

[bu orgs-auth user-add add organization role to a user id: organization
uuid role: organization role ]{.c1}

[user: authorization user ]{.c1}

[bu orgs-auth user-del remove organization role from a user id:
organization uuid role: organization role ]{.c1}

[user: authorization user ]{.c1}

[bu orgs-auth user-get get organization users id: organization uuid
]{.c1}

[bu service-catalogs   (service catalog management) ]{.c2}

[bu service-catalogs add add service catalog name: service catalog name
-desc: service catalog description ]{.c1}

[bu service-catalogs definition-add ]{.c1}

[bu service-catalogs definition-del ]{.c1}

[delete service catalog service definition id: service catalog id ]{.c1}

[definitions: comma separated list of definition id ]{.c1}

[delete service catalog service definition id: service catalog id ]{.c1}

[definitions: comma separated list of definition id ]{.c1}

[bu service-catalogs delete delete service catalog id: service catalog
id ]{.c1}

[bu service-catalogs get get srvcatalogs -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: service catalog id ]{.c1}

[-objid: authorization id ]{.c1}

[-name: service catalog name ]{.c1}

[bu service-catalogs patch refresh service catalog id: service catalog
id ]{.c1}

[bu service-catalogs update update service catalog id: service catalog
id -name: service catalog name ]{.c1}

[-desc: service catalog description ]{.c1}

[bu service-catalogs-auth   (service catalog authorization) ]{.c2}

[bu service-catalogs-auth group-add ]{.c1}

[bu service-catalogs-auth group-del ]{.c1}

[bu service-catalogs-auth group-get ]{.c1}

[bu service-catalogs-auth role-get ]{.c1}

[bu service-catalogs-auth user-add ]{.c1}

[bu service-catalogs-auth user-del ]{.c1}

[bu service-catalogs-auth user-get ]{.c1}

[add service catalog role to a group id: service catalog id role:
service catalog role ]{.c1}

[group: authorization group ]{.c1}

[remove service catalog role from a group id: service catalog id role:
service catalog role ]{.c1}

[group: authorization group ]{.c1}

[get service catalog groups id: service catalog id get service catalog
roles id: service catalog id ]{.c1}

[add service catalog role to a user id: service catalog id role: service
catalog role ]{.c1}

[user: authorization user ]{.c1}

[remove service catalog role from a user id: service catalog id role:
service catalog role ]{.c1}

[user: authorization user ]{.c1}

[get service catalog users id: service catalog id ]{.c1}

[bu service-consumes   (service consume management) ]{.c2}

[bu service-consumes aggregate ]{.c1}

[generate aggregated consume period: aggregation period. Ex. YYYY-MM o
YYYY-MM-GG ]{.c1}

[bu service-consumes get list service job schedule -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\]]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: consume id ]{.c1}

[-type: consume type id ]{.c1}

[-account: account id ]{.c1}

[-aggr\_type: aggregation type ]{.c1}

[-period: aggregation period ]{.c1}

[-task: execution task ]{.c1}

[-date\_start: start date ]{.c1}

[-date\_end: stop date ]{.c1}

[bu service-defs   (service definition management) ]{.c2}

[bu service-defs add add service definition name: service definition
name type: service type id ]{.c1}

[params: service definition params ]{.c1}

[-desc: service definition description ]{.c1}

[-version: service definition version ]{.c1}

[-status: service definition status ]{.c1}

[bu service-defs delete delete service definition id: service definition
id ]{.c1}

[bu service-defs get get service definitions -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-name: entity name ]{.c1}

[-objid: authorization id ]{.c1}

[-version: definition version ]{.c1}

[-status: type status ]{.c1}

[bu service-defs update update service definition id: service definition
id ]{.c1}

[-name: service definition name ]{.c1}

[-desc: service definition description ]{.c1}

[-status: service definition status ]{.c1}

[-config: service definition config key:value ]{.c1}

[bu service-insts   (service instance management) ]{.c2}

[bu service-insts check check service instance -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[bu service-insts config-set update resource entity config id: resource
entity id ]{.c1}

[key: config key like config.key ]{.c1}

[-value: config value ]{.c1}

[bu service-insts delete delete service instance -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[-propagate: if True propagate delete to all cmp modules ]{.c1}

[\[default=false\] ]{.c1}

[-force: if True force delete \[default=false\] ]{.c1}

[bu service-insts filter get service instances user\_name: user name
]{.c1}

[bu service-insts get get service instances -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-legacy: use legacy v1 ]{.c1}

[-name: entity name ]{.c1}

[-objid: authorization id ]{.c1}

[-version: definition version ]{.c1}

[-status: type status ]{.c1}

[-account: account id ]{.c1}

[-resource: resource uuid ]{.c1}

[-parent: parent service instance ]{.c1}

[-plugintype: service plugintype ]{.c1}

[-tags: comma separated tag list ]{.c1}

[-iscontainer: if True show only container service instance ]{.c1}

[bu service-insts import from-resource ]{.c1}

[import service instance from resource name: service instance name
-desc: service instance description ]{.c1}

[account: account id ]{.c1}

[plugintype: plugin type of the service instance ]{.c1}

[container\_plugintype: plugin type of the container ]{.c1}

[-service\_definition\_id: service definition id ]{.c1}

[resource: resource id]{.c1}

[-parent: parent service instance id ]{.c1}

[bu service-insts patch patch service instance -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[bu service-insts status update service instance status -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[status: service instance status ]{.c1}

[bu service-insts tag-add add tag to service instance -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[tags: comma separated list of tags ]{.c1}

[bu service-insts tag-del delete tag from service instance -size: list
page size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[tags: comma separated list of tags ]{.c1}

[bu service-insts tag-get get tag of service instance id: service
instance id ]{.c1}

[bu service-insts update update service instance -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: service instance id ]{.c1}

[-resource\_uuid: resource uuid ]{.c1}

[-parent: parent service instance ]{.c1}

[-name: service instance name ]{.c1}

[bu service-links   (service link management) ]{.c2}

[bu service-links add add service link name: service link name account:
account id ]{.c1}

[type: service link type ]{.c1}

[start\_service: start service uuid ]{.c1}

[end\_service: end service uuid ]{.c1}

[-attributes: service link attributes ]{.c1}

[bu service-links delete delete service links ids: comma separated
service link uuids -force: if true force the delete ]{.c1}

[bu service-links get list service links -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: link uuid ]{.c1}

[-name: link name ]{.c1}

[-service: start or end service uuid ]{.c1}

[-type: link type ]{.c1}

[-objid: link authorization id ]{.c1}

[-tags: link tags ]{.c1}

[bu service-links tag-add add tag to service link id: service link id
tag: tag ]{.c1}

[bu service-links tag-del delete tag from service link id: service link
id tag: tag ]{.c1}

[bu service-links tag-get get tag of service link id: service link id
]{.c1}

[bu service-links update update service link id: service link uuid
-name: service link name ]{.c1}

[-type: service link type ]{.c1}

[-start\_service: start service uuid ]{.c1}

[-end\_service: end service uuid ]{.c1}

[-attributes: service link attributes ]{.c1}

[bu service-metrics   (service metric management) ]{.c2}

[bu service-metrics acquire acquire metric -account: account id -type:
metric type ]{.c1}

[-service: metric service instance id]{.c1}

[bu service-metrics get list service metrics -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: metric id ]{.c1}

[-day: sample day ]{.c1}

[-value: metric value ]{.c1}

[-num: metric num ]{.c1}

[-service: metric service instance id ]{.c1}

[-type: metric type ]{.c1}

[-jobid: sample job id ]{.c1}

[bu service-metrics type-add add service metric type name: metric type
name ]{.c1}

[-desc: metric type description ]{.c1}

[-group: metric type group ]{.c1}

[type: metric type. Supported values: ]{.c1}

[CONSUME\|BUNDLE\|OPT\_BUNDLE\|PROF\_SERVICE ]{.c1}

[-unit: metric type unit ]{.c1}

[-status: metric type status ]{.c1}

[-active: metric type active ]{.c1}

[-limits: json file with limit definition.Ex. {\"limits\" : \[{ \"name\"
: ]{.c1}

[\"LimitCPU\", \"desc\" : \"LimitCPU\", \"value\": 2.0,
\"metric\_type\_id\" : \"1\" ]{.c1}

[}\]} ]{.c1}

[bu service-metrics type delete ]{.c1}

[delete service metric types -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: metric type id ]{.c1}

[bu service-metrics type-get list service metric types -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: metric type id ]{.c1}

[-name: metric type name ]{.c1}

[-group: metric type group name ]{.c1}

[-type: metric type ]{.c1}

[bu service-metrics type update ]{.c1}

[update service metric type -id: metric type id ]{.c1}

[-name: metric type name ]{.c1}

[-desc: metric type description ]{.c1}

[-group: metric type group ]{.c1}

[-type: metric type. Supported values: ]{.c1}

[CONSUME\|BUNDLE\|OPT\_BUNDLE\|PROF\_SERVICE ]{.c1}

[-unit: metric type unit ]{.c1}

[-status: metric type status ]{.c1}

[-active: metric type active ]{.c1}

[-limits: json file with limit definition.Ex. {\"limits\" : \[{ \"name\"
: ]{.c1}

[\"LimitCPU\", \"desc\" : \"LimitCPU\", \"value\": 2.0,
\"metric\_type\_id\" : \"1\" ]{.c1}

[}\]} ]{.c1}

[bu service-schedules   (service schedule management) ]{.c2}

[bu service-schedules add add service job schedule config: job schedule
config file ]{.c1}

[bu service-schedules add example ]{.c1}

[list service job schedule ]{.c1}

[bu service-schedules delete delete service job schedule -id: job
schedule id ]{.c1}

[bu service-schedules get list service job schedule -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: job schedule id ]{.c1}

[-name: job schedule name ]{.c1}

[-job\_name: job schedule job name ]{.c1}

[-job\_id: job schedule job id ]{.c1}

[-type: job schedule type ]{.c1}

[-metric\_type: job schedule metric type ]{.c1}

[bu service-schedules restart restart service job schedule -id: job
schedule id bu service-schedules start start service job schedule -id:
job schedule id bu service-schedules stop stop service job schedule -id:
job schedule id ]{.c1}

[bu service-tags   (service tag management) ]{.c2}

[bu service-tags add add service tag value: service tag value account:
account id]{.c1}

[bu service-tags delete delete service tags ids: comma separated service
tag id -force: if true force the delete ]{.c1}

[bu service-tags get list service tags -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-value: tag value ]{.c1}

[-service: service id ]{.c1}

[-link: service link id ]{.c1}

[bu service-tags update update service tag id: service tag uuid -value:
service tag value ]{.c1}

[bu service-types   (service type management) ]{.c2}

[bu service-types add add service type name: service type name objclass:
python class full path ]{.c1}

[-version: service type version ]{.c1}

[-flag\_container: if True service is a container ]{.c1}

[-status: service type status ]{.c1}

[bu service-types delete delete service type ids: service type id ]{.c1}

[bu service-types get get service types -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-name: entity name ]{.c1}

[-objid: authorization id ]{.c1}

[-version: type version ]{.c1}

[-status: type status ]{.c1}

[bu service-types plugin-get get service type plugins -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[bu service-types process get ]{.c1}

[get service type process id: service type id ]{.c1}

[bu service-types process-set set service type process id: service type
id ]{.c1}

[method: service type process method ]{.c1}

[-name: name ]{.c1}

[-desc: description ]{.c1}

[-process: process ]{.c1}

[-template: template file ]{.c1}

[bu service-types update update service type id: service type id ]{.c1}

[-name: service type name ]{.c1}

[-objclass: python class full path ]{.c1}

[-version: service type version ]{.c1}

[-flag\_container: if True service is a container ]{.c1}

[-status: service type status ]{.c1}

[bu staas   (storage service management) ]{.c2}

[bu staas info get storage service info account: account id ]{.c1}

[bu staas quotas get storage service quotas account: account id ]{.c1}

[bu staas efs   (file share service management) ]{.c83}

[bu staas efs add create a share name: share name ]{.c1}

[account: parent account id ]{.c1}

[size: share size ]{.c1}

[-type: share type ]{.c1}

[-mode: share performance mode. Can be generalPurpose or ]{.c1}

[localPurpose ]{.c1}

[bu staas efs delete delete a share share: share id ]{.c1}

[bu staas efs get get share share: share id ]{.c1}

[bu staas efs grant-add create a share grant share: share id ]{.c1}

[access\_level: access to grant shld be rw \| r ]{.c1}

[access\_type: access type should be ip ]{.c1}

[access\_to: access to expression ]{.c1}

[bu staas efs grant-delete delete share grant share: share id ]{.c1}

[grant: grant id]{.c1}

[bu staas efs list list share -accounts: list of account id comma
separated -name: list of share id comma separated ]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu staas efs resize resize a share share: share id ]{.c1}

[size: new share size in GB ]{.c1}

[bu staas efs target-add create share mount target share: share id
]{.c1}

[subnet: share subnet ]{.c1}

[protocol: protocol should be nfs\|cifs ]{.c1}

[-label: custom label to be used when you want to use a labelled share
]{.c1}

[type ]{.c1}

[-ontap\_volume: ontap netapp volume id ]{.c1}

[bu staas efs target-delete delete share mount target share: share id
]{.c1}

[bu staas efs target-list list share mount target -accounts: list of
account id comma separated -name: list of share id comma separated
]{.c1}

[-tags: list of tag comma separated ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[bu staas efs types get share types ]{.c1}

[catalogs   (api catalog management) ]{.c301}

[catalogs add add catalog name: catalog name ]{.c1}

[zone: catalog zone ]{.c1}

[catalogs add-endpoint add catalog endpoint name: catalog endpoint name
]{.c1}

[catalog: catalog uuid ]{.c1}

[service: service name like auth or resource ]{.c1}

[uri: service uri ]{.c1}

[catalogs delete delete catalog id: catalog uuid ]{.c1}

[catalogs delete-endpoint delete catalog endpoint id: catalog endpoint
uuid ]{.c1}

[catalogs get get catalogs -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: catalog uuid ]{.c1}

[catalogs get-endpoints get catalog endpoints -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: catalog endpoint uuid ]{.c1}

[catalogs ping-endpoint ping catalog endpoint id: catalog endpoint uuid
]{.c1}

[catalogs ping-endpoints ping catalog endpoints id: catalog uuid ]{.c1}

[dq-res   (resource data quality) ]{.c301}

[dq-res dq-entities   (entities data quality) ]{.c2}

[dq-res dq-entities bad-get get bad resources -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-definition: entity definition ]{.c1}

[dq-res dq-entities bad remove ]{.c1}

[get bad resources -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: entity id ]{.c1}

[dq-res dq-entities check check resource entities -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-name: entity name ]{.c1}

[-desc: entity description]{.c1}

[dq-res dq-entities check compute-instance ]{.c1}

[dq-res dq-entities compute volume-check ]{.c1}

[dq-res dq-entities compute volume-repair ]{.c1}

[-container: container uuid or name ]{.c1}

[-type: entity type ]{.c1}

[-objid: entity authorization id ]{.c1}

[-ext\_id: entity physical id ]{.c1}

[-parent: entity parent ]{.c1}

[-state: entity state ]{.c1}

[-attributes: entity attributes ]{.c1}

[-tags: entity tags ]{.c1}

[check compute instance -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-hypervisor: hypervisor ]{.c1}

[-name: name filter ]{.c1}

[repair compute volume tree -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-definition: entity definition ]{.c1}

[repair compute volume tree -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-definition: entity definition ]{.c1}

[dq-res dq-entities remove remove bad resource -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: entity id ]{.c1}

[dq-res dq-links   (links data quality) ]{.c2}

[dq-res dq-links bad-get get bad links -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-definition: entity definition ]{.c1}

[dq-res dq-links bad-remove get bad links -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: link id ]{.c1}

[dq-res dq-links check repair resource links -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: link id ]{.c1}

[dq-res dq-links remove remove bad link -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: link id ]{.c1}

[dq-service   (service data quality) ]{.c301}

[dq-service dq-insts   (service instance data quality) ]{.c2}

[dq-service dq-insts check check service instances -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-name: entity name ]{.c1}

[-desc: entity description ]{.c1}

[-container: container uuid or name ]{.c1}

[-type: entity type ]{.c1}

[-objid: entity authorization id ]{.c1}

[-ext\_id: entity physical id ]{.c1}

[-parent: entity parent ]{.c1}

[-state: entity state ]{.c1}

[-attributes: entity attributes]{.c1}

[-tags: entity tags ]{.c1}

[mgmt   (Administration and objects management) ]{.c301}

[mgmt database   (database administartion commands) ]{.c2}

[mgmt database check check database storage database: database service
id uuid or name this is one of the serivce identifiers ]{.c1}

[\--tofile: store to file only when format is json or yaml ]{.c1}

[mgmt loadbalancers   (loadbalancer administration commands) ]{.c2}

[mgmt loadbalancers delete delete load balancer id: load balancer id
]{.c1}

[-no-linked-objs: Use this option to avoid deleting service instances
like ]{.c1}

[target group and custom listener linked to load balancer ]{.c1}

[-no-physical-resources: Use this option to delete only CMP metadata
]{.c1}

[without deleting physical resources ]{.c1}

[mgmt loadbalancers load import load balancer appliance: network
appliance (e.g. nsx edge) uuid -account: the uuid of the account owner
of the virtual server(s) to ]{.c1}

[import ]{.c1}

[-virtual-server: the name of the virtual server to import ]{.c1}

[platform   (platform management) ]{.c301}

[platform check check platform status -engines: engine name ]{.c1}

[platform version get platform versions -engine: engine name ]{.c1}

[platform awx   (awx platform management) ]{.c2}

[platform awx ad-hoc command-add ]{.c1}

[platform awx ad-hoc command-get ]{.c1}

[platform awx ad-hoc command-relaunch ]{.c1}

[platform awx ad-hoc command-stdout ]{.c1}

[add add hoc commands -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[inventory: inventory id ]{.c1}

[credential: credential id ]{.c1}

[-verbosity: verbosity ]{.c1}

[get add hoc commands -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-inventory: inventory id ]{.c1}

[-id: job id ]{.c1}

[relaunch add hoc command -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[get add hoc command stdout -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[platform awx credential-del delete credential -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: credential id ]{.c1}

[platform awx credential-get get credentials -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\]]{.c1}

[platform awx credential-git add ]{.c1}

[platform awx credential ssh-add ]{.c1}

[platform awx credential type-get ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: credential id ]{.c1}

[-name: credential name ]{.c1}

[add git credential -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: credential name ]{.c1}

[organization: organization id ]{.c1}

[username: username ]{.c1}

[password: password ]{.c1}

[add ssh credential -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: credential name ]{.c1}

[organization: organization id ]{.c1}

[username: username ]{.c1}

[-password: password ]{.c1}

[-key\_data: ssh key data file ]{.c1}

[-key\_unlock: ssh key unlock ]{.c1}

[-become: become method ]{.c1}

[get credential types -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: credential type id ]{.c1}

[platform awx host-add add host -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: host name ]{.c1}

[inventory: inventory id ]{.c1}

[-desc: host description ]{.c1}

[-vars: host variables. ex: k1:v1,k2:v2 ]{.c1}

[platform awx host-del delete host -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: host id ]{.c1}

[platform awx host-get get hosts -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: host id ]{.c1}

[-name: host name ]{.c1}

[platform awx host-group add ]{.c1}

[platform awx host-group del ]{.c1}

[add group to host -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: host id ]{.c1}

[group: group id ]{.c1}

[remove group from host -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: host id ]{.c1}

[group: group id ]{.c1}

[platform awx inventory-add add inventory -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: inventory name ]{.c1}

[organization: organization id]{.c1}

[platform awx inventory-del delete inventory -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: inventory id ]{.c1}

[platform awx inventory-get get inventories -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: inventory id ]{.c1}

[-name: inventory name ]{.c1}

[platform awx inventory group-add ]{.c1}

[platform awx inventory group-del ]{.c1}

[platform awx inventory group-get ]{.c1}

[platform awx inventory host-get ]{.c1}

[platform awx inventory script-add ]{.c1}

[platform awx inventory script-del ]{.c1}

[platform awx inventory script-get ]{.c1}

[platform awx inventory source-sync ]{.c1}

[platform awx job-event error-get ]{.c1}

[add inventory group -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[inventory: inventory id ]{.c1}

[name: inventory group name ]{.c1}

[-desc: host description ]{.c1}

[-vars: host variables. ex: k1:v1,k2:v2 ]{.c1}

[delete inventory group -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: inventory group id ]{.c1}

[get inventory groups -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: inventory group id ]{.c1}

[-name: inventory name ]{.c1}

[-inventory: inventory id ]{.c1}

[get inventory hosts -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: inventory group id ]{.c1}

[-name: inventory name ]{.c1}

[-inventory: inventory id ]{.c1}

[add script inventory -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: script inventory name ]{.c1}

[organization: organization id ]{.c1}

[script: script. Ex. \#!/bin/bash source /opt/beehive/bin/activate
]{.c1}

[delete script inventory -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: inventory id ]{.c1}

[get inventory scripts -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-inventory: inventory id ]{.c1}

[-id: group id ]{.c1}

[sync inventory source -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: inventory source id ]{.c1}

[get job error -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[platform awx job-event-get get job events -size: list page size
\[default=20\] -page: list page \[default=0\]]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[-query: job event query. Comma separated k:v ]{.c1}

[platform awx job-get get jobs -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: job id ]{.c1}

[platform awx job-relaunch relaunch job -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[platform awx job-stdout get job stdout -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: job id ]{.c1}

[platform awx org-get get organizations -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: organization id ]{.c1}

[-name: organization name ]{.c1}

[platform awx ping ping awx -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[platform awx project-add add project -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: project name ]{.c1}

[organization: organization id ]{.c1}

[credential: credential id ]{.c1}

[scm\_url: scm url ]{.c1}

[-scm\_type: scm type ]{.c1}

[-scm\_branch: scm branch ]{.c1}

[-scm\_update\_on\_launch: scm update on launch ]{.c1}

[platform awx project-del delete project -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: project id ]{.c1}

[platform awx project-get get projects -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: project id ]{.c1}

[-name: project name ]{.c1}

[platform awx project-job event-get ]{.c1}

[platform awx project-job get ]{.c1}

[platform awx project-job stdout ]{.c1}

[get project job events -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: project job id ]{.c1}

[get project job -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: project job id ]{.c1}

[get project job stdout -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: project job id]{.c1}

[platform awx project-sync sync project -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: project id ]{.c1}

[platform awx template-add add template -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[name: template name ]{.c1}

[inventory: inventory id ]{.c1}

[project: project id ]{.c1}

[playbook: playbook ]{.c1}

[-verbosity: verbosity: 0 (Normal) (default), 1 (Verbose), 2 (More
]{.c1}

[Verbose), 3 (Debug), 4 (Connection Debug), 5 (WinRM Debug) ]{.c1}

[platform awx template-del delete template -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: template id ]{.c1}

[platform awx template-get get templates -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[-id: template id ]{.c1}

[-name: template name ]{.c1}

[platform awx template launch ]{.c1}

[launch template -size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[id: template id ]{.c1}

[credentials: comma separated credentials id ]{.c1}

[-extras: variables used when launching job template, k1:v1;k2:v2 ]{.c1}

[platform awx version get awx version -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: awx platform reference label ]{.c1}

[platform cmp customize   (cmp customization) ]{.c83}

[platform cmp customize get get available configurations ]{.c1}

[platform cmp customize run run customization. This command can be used
many times to add new items ]{.c1}

[config: config file ]{.c1}

[-filter: filter to apply ::. Ex. ]{.c1}

[resource.entities.site\_networks:name:NVLP3-Prov-WEB2-test -sections:
comma separated list of section to execute ]{.c1}

[platform cmp customize show ]{.c1}

[show configuration config: config file ]{.c1}

[-filter: filter to apply ::. Ex. ]{.c1}

[resource.entities.site\_networks:name:NVLP3-Prov-WEB2-test ]{.c1}

[platform cmp logs   (cmp logs management) ]{.c83}

[platform cmp logs api get api request received -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-index: index name ]{.c1}

[-id: api request id ]{.c1}

[-uri: api request ri. uri:method ]{.c1}

[-user: api request source user ]{.c1}

[-ip: api request source ip ]{.c1}

[-sort: sort field. Ex. \@timestamp:desc ]{.c1}

[platform cmp logs engine show log for cmp engine -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-index: index name ]{.c1}

[-name: container partial name. Ex. uwsgi-auth, worker-auth, uwsgi-ssh
]{.c1}

[-sort: sort field. Ex. date:desc ]{.c1}

[-pod: pod name ]{.c1}

[-op: oepration id. Can be api\_id, task\_id, task\_id:step\_name ]{.c1}

[platform cmp logs event show cmp events -size: list page size
\[default=20\]]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-index: index name ]{.c1}

[-kvargs: kvargs like query string ]{.c1}

[-id: event id ]{.c1}

[-type: event id ]{.c1}

[-sort: sort field. Ex. date:desc ]{.c1}

[platform cmp post-install   (DEPRECATED - cmp post install management)
]{.c83}

[platform cmp post-install get ]{.c1}

[platform cmp post-install run ]{.c1}

[get post install available configurations ]{.c1}

[run post install. This command can be used many times to add new items
]{.c1}

[config: config file ]{.c1}

[-filter: filter to apply ::. Ex. ]{.c1}

[resource.entities.site\_networks:name:NVLP3-Prov-WEB2-test -sections:
comma separated list of section to execute ]{.c1}

[platform cmp post-install show ]{.c1}

[get post install available configurations config: config file ]{.c1}

[-filter: filter to apply ::. Ex. ]{.c1}

[resource.entities.site\_networks:name:NVLP3-Prov-WEB2-test ]{.c1}

[platform cmp subsystems   (cmp subsystems management) ]{.c83}

[platform cmp subsystems create ]{.c1}

[platform cmp subsystems deploy ]{.c1}

[platform cmp subsystems get ]{.c1}

[platform cmp subsystems redeploy ]{.c1}

[platform cmp subsystems runtime-api-spec ]{.c1}

[platform cmp subsystems runtime-apidocs ]{.c1}

[platform cmp subsystems runtime-capabilities ]{.c1}

[platform cmp subsystems runtime-get ]{.c1}

[platform cmp subsystems runtime-log ]{.c1}

[platform cmp subsystems runtime-ping ]{.c1}

[platform cmp subsystems runtime-version ]{.c1}

[create cmp subsystem structure (db, data) subsystem: subsystem. Ex.
resource, service file: subsystem config file full path ]{.c1}

[deploy cmp subsystem -subsystem: subsystem. Ex. resource, service get
cmp subsystem config -id: subsystem. Ex. resource, service ]{.c1}

[redeploy cmp subsystem subsystem: subsystem. Ex. resource, service
-path: remote package path ]{.c1}

[-pkgs: list of package to sync ]{.c1}

[get cmp instance openapi spec id: subsystem. Ex. resource, service
]{.c1}

[get cmp instance swagger web interface id: subsystem. Ex. resource,
service ]{.c1}

[get cmp instance capabilities id: subsystem. Ex. resource, service
]{.c1}

[get cmp subsystems -id: subsystem. Ex. resource, service ]{.c1}

[-role: deployment role ]{.c1}

[get cmp subsystem pod log subsystem: subsystem. e.g. resource, service
role: deployment role. e.g. uwsgi ]{.c1}

[-follow: follow log. Default: true. ]{.c1}

[-lines: number of log lines to show. Default: 100. Ignored when follow
]{.c1}

[is true. ]{.c1}

[ping cmp subsystems -id: subsystem. Ex. resource, service ]{.c1}

[-role: deployment role ]{.c1}

[get cmp instance versions id: subsystem. Ex. resource, service ]{.c1}

[platform cmp subsystems sync ]{.c1}

[update cmp nivola python packages - use with devel env ]{.c1}

[-path: remote package path -pkgs: list of package to sync ]{.c1}

[platform cmp subsystems undeploy ]{.c1}

[undeploy cmp subsystem -subsystem: subsystem. Ex. resource, service
]{.c1}

[platform cmp subsystems update ]{.c1}

[update cmp subsystem structure (db, data) ]{.c1}

[subsystem: subsystem. Ex. resource, service file: subsystem config file
full path ]{.c1}

[platform cmp tests   (cmp test management) ]{.c83}

[platform cmp tests get list cmp regression tests -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-package: python package ]{.c1}

[-plan: name of the test plan ]{.c1}

[-group: name of the sub test group ]{.c1}

[platform cmp tests run run cmp regression tests -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-package: python package ]{.c1}

[-plan: name of the test plan ]{.c1}

[-group: name of the sub test group]{.c1}

[-list: list of test id to run ]{.c1}

[-test: name of test to run ]{.c1}

[-mainconf: optional main test configuration ]{.c1}

[-conf: optional extra test configuration ]{.c1}

[-validate: if True enable api validation in test ]{.c1}

[-user: user used to run test. Ex. test1, admin \[default=test1\] ]{.c1}

[-concurrency: specify how many tests run in parallel for massive test
]{.c1}

[\[default=2\] ]{.c1}

[platform console   (console management) ]{.c2}

[platform console connect connect to console -C, \--console: console
label ]{.c1}

[-user: user name ]{.c1}

[-pwd: user password required ]{.c1}

[platform console update update shell console -C, \--console: console
label ]{.c1}

[-pkgs: user name ]{.c1}

[platform console user-env add ]{.c1}

[setup user additional environment -C, \--console: console label ]{.c1}

[user\_ssh: console user ]{.c1}

[user\_env: comma separated list of environment to add ]{.c1}

[platform console user-get list user configured -C, \--console: console
label user: user name ]{.c1}

[platform console user-list list user configured -C, \--console: console
label ]{.c1}

[platform console user-setup setup user home directory and configuration
]{.c1}

[-C, \--console: console label user\_ssh: console user ]{.c1}

[platform console user update ]{.c1}

[update user base config -C, \--console: console label user\_ssh:
console user ]{.c1}

[-isadmin: console user ]{.c1}

[platform console versions get cmp packages version -C, \--console:
console label ]{.c1}

[platform datadomain   (datadomain management) ]{.c2}

[platform datadomain info info from datadomain ]{.c1}

[platform datadomain mtree get ]{.c1}

[platform datadomain ]{.c1}

[network-get ]{.c1}

[get datadomain mtrees -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[-mtree\_id: data domain mtree id ]{.c1}

[get datadomain networks -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[-network\_id: data domain network id ]{.c1}

[platform datadomain ping ping datadomain instances -port: datadomain
port ]{.c1}

[platform datadomain protocol-nfs-add ]{.c1}

[platform datadomain protocol-nfs-client-add ]{.c1}

[platform datadomain protocol-nfs-client-del ]{.c1}

[platform datadomain protocol-nfs-get ]{.c1}

[add datadomain nfs exports -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[mtree: mtree name ]{.c1}

[path: data domain nfs export path ]{.c1}

[add datadomain nfs export client -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[nfs\_id: data domain nfs exports id ]{.c1}

[client: client fqdn ]{.c1}

[delete datadomain nfs export client -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[nfs\_id: data domain nfs exports id ]{.c1}

[client: client fqdn ]{.c1}

[get datadomain nfs exports -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id]{.c1}

[platform datadomain services-get ]{.c1}

[platform datadomain setting-get ]{.c1}

[platform datadomain tenant-get ]{.c1}

[platform datadomain trust get ]{.c1}

[platform datadomain user get ]{.c1}

[-nfs\_id: data domain nfs exports id ]{.c1}

[get datadomain services id: data domain system id get datadomain
settings id: data domain system id ]{.c1}

[get datadomain tenants -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[-tenant\_id: data domain tenant id ]{.c1}

[get datadomain trust -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[get datadomain users -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: data domain system id ]{.c1}

[-user\_id: data domain user id ]{.c1}

[platform dns   (dns platform) ]{.c2}

[platform dns ping ping dns -O, \--orchestrator: dns platform reference
label -P, \--project: dns current project name ]{.c1}

[platform dns version get dns version -O, \--orchestrator: dns platform
reference label -P, \--project: dns current project name ]{.c1}

[platform dns zone-alias query ]{.c1}

[get fqdn address form alias -O, \--orchestrator: dns platform reference
label -P, \--project: dns current project name ]{.c1}

[alias: alias ]{.c1}

[-group: dns group. Can be resolver or update \[default=resolver\]
]{.c1}

[platform dns zone authority-get ]{.c1}

[the SOA (Start of Authority) used to manage the zone ]{.c1}

[-O, \--orchestrator: dns platform reference label -P, \--project: dns
current project name id: zone ]{.c1}

[platform dns zone-fqdn query ]{.c1}

[get ip address form fqdn -O, \--orchestrator: dns platform reference
label -P, \--project: dns current project name ]{.c1}

[fqdn: fqdn ]{.c1}

[-group: dns group. Can be resolver or update \[default=resolver\]
]{.c1}

[platform dns zone-get get all the managed zones -O, \--orchestrator:
dns platform reference label -P, \--project: dns current project name
]{.c1}

[platform dns zone nameserver-get ]{.c1}

[get all the nameservers that resolve the zone ]{.c1}

[-O, \--orchestrator: dns platform reference label -P, \--project: dns
current project name id: zone ]{.c1}

[platform dns zone orchestrator-get ]{.c1}

[get all the configured orchestrators -O, \--orchestrator: dns platform
reference label -P, \--project: dns current project name ]{.c1}

[platform elastic   (elastic management) ]{.c2}

[platform elastic cluster health ]{.c1}

[platform elastic cluster nodes ]{.c1}

[platform elastic cluster stats ]{.c1}

[get cluster health get cluster nodes get cluster statistics ]{.c1}

[platform elastic index-count count index documents -size: list page
size \[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[index: index name ]{.c1}

[-query: simple query like field1:value1 ]{.c1}

[-sort: sort field. Ex. date:desc\] ]{.c1}

[-fields: comma separated list of fields to show ]{.c1}

[platform elastic index-del delete index index: index name ]{.c1}

[platform elastic index-get get indexes -index: index name -pattern:
index pattern ]{.c1}

[platform elastic index-list list indexes -pattern: index pattern]{.c1}

[platform elastic index-query query index -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[index: index name ]{.c1}

[-query: simple query like field1:value1 ]{.c1}

[-sort: sort field. Ex. date:desc\] ]{.c1}

[-fields: comma separated list of fields to show ]{.c1}

[platform elastic index-stats get index statistics index: index name
]{.c1}

[platform elastic info get elastic info ]{.c1}

[platform elastic ping ping elastic ]{.c1}

[platform elastic role mapping-add ]{.c1}

[platform elastic role mapping-del ]{.c1}

[platform elastic role mapping-get ]{.c1}

[add role mapping name: role mapping name role\_name: role name ]{.c1}

[user\_email: user email ]{.c1}

[realm\_name: realm name ]{.c1}

[delete role mapping name: role mapping name get role mapping -name:
role mapping name ]{.c1}

[platform elastic user-add add user name: user name ]{.c1}

[password: password ]{.c1}

[role: role ]{.c1}

[-full\_name: full\_name ]{.c1}

[-email: full\_name ]{.c1}

[platform elastic user-del delete user name: user name ]{.c1}

[platform elastic user-get get user -name: user name ]{.c1}

[platform fwlog   (firewall logs management) ]{.c2}

[platform fwlog dfw show log for dfw -O, \--orchestrator: mysql cluster
or single node reference label -size: list page size \[default=20\]
]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-index: index name ]{.c1}

[-reject: if true show only reject ]{.c1}

[-sort: sort field. Ex. \@timestamp:desc ]{.c1}

[-pretty: if true show pretty logs ]{.c1}

[-ip: ip address ]{.c1}

[platform fwlog edge show log for edge -O, \--orchestrator: mysql
cluster or single node reference label -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[edge: edge name ]{.c1}

[-type: log type: firewall, config, nat, ]{.c1}

[-index: index name ]{.c1}

[-reject: if true show only reject ]{.c1}

[-sort: sort field. Ex. \@timestamp:desc ]{.c1}

[-pretty: if true show pretty logs ]{.c1}

[-ip: ip address ]{.c1}

[platform grafana   (grafana platform management) ]{.c2}

[platform grafana alert notification-add ]{.c1}

[platform grafana alert notification-del ]{.c1}

[platform grafana alert notification-get ]{.c1}

[add alert notification -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[name: alert notification name ]{.c1}

[email: alert notification email ]{.c1}

[delete alert notification -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: alert notification uid ]{.c1}

[get alert notification -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-id: alert notification uid ]{.c1}

[-name: alert notification name]{.c1}

[platform grafana alert notification-update ]{.c1}

[platform grafana ]{.c1}

[dashboard-add ]{.c1}

[platform grafana ]{.c1}

[dashboard-copy ]{.c1}

[platform grafana ]{.c1}

[dashboard-del ]{.c1}

[platform grafana ]{.c1}

[dashboard-get ]{.c1}

[update alert notification -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: alert notification uid ]{.c1}

[name: alert notification name ]{.c1}

[email: alert notification email ]{.c1}

[add dashboard -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[data\_dashboard: dashboard data ]{.c1}

[copy dashboard -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[name: dashboard name to search ]{.c1}

[folder\_uid: folder uid where add dashboard ]{.c1}

[organization: organization name ]{.c1}

[division: division name ]{.c1}

[account: account name ]{.c1}

[delete dashboard -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: dashboard id ]{.c1}

[get dashboard -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-id: dashboard uid ]{.c1}

[-search: dashboard search query ]{.c1}

[-folder: folder id - 0 for General ]{.c1}

[platform grafana folder-add add folder -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[name: folder name ]{.c1}

[platform grafana folder dashboard-get ]{.c1}

[get folder dashboard -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: folder uid or \"general\" for general folder ]{.c1}

[-search: dashboard search query ]{.c1}

[platform grafana folder-del delete folder -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[uid: folder uid ]{.c1}

[platform grafana folder-get get folder -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-uid: folder uid ]{.c1}

[-name: folder name ]{.c1}

[platform grafana folder permission-add ]{.c1}

[add folder permission -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[uid: folder uid ]{.c1}

[-team\_viewer: team id viewer ]{.c1}

[-team\_editor: team id editor]{.c1}

[platform grafana folder permission-get ]{.c1}

[add folder permission -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[uid: folder uid ]{.c1}

[-team\_viewer: team id viewer ]{.c1}

[-team\_editor: team id editor ]{.c1}

[platform grafana ping ping grafana -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[platform grafana team-add add team -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[name: team name ]{.c1}

[platform grafana team-del delete team -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: team id ]{.c1}

[platform grafana team-get get team -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-id: team id ]{.c1}

[-name: team name ]{.c1}

[platform grafana team-user add ]{.c1}

[platform grafana team-user del ]{.c1}

[platform grafana team-user get ]{.c1}

[add user to team -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[team\_id: team id ]{.c1}

[user\_id: user id ]{.c1}

[delete user from team -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[team\_id: team id ]{.c1}

[user\_id: user id ]{.c1}

[get user of team -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: team id ]{.c1}

[platform grafana user-add add user -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-name: user name ]{.c1}

[-email: email ]{.c1}

[-login: user login ]{.c1}

[-password: password ]{.c1}

[platform grafana user-del delete user -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[id: user id ]{.c1}

[platform grafana user-get get user -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[-id: user uid ]{.c1}

[-name: user name]{.c1}

[platform grafana version get grafana version -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: grafana platform reference label ]{.c1}

[platform graphite   (graphite management) ]{.c2}

[platform graphite vm metric ]{.c1}

[platform graphite vm metric-highest ]{.c1}

[platform graphite vm metric-one ]{.c1}

[get vm metrics ip\_address\_graphite: ip address graphite pod: pod name
]{.c1}

[vm: vm name ]{.c1}

[metrics: metric ]{.c1}

[function: function ]{.c1}

[period: period ]{.c1}

[get vm highest metrics ip\_address\_graphite: ip address graphite pod:
pod name ]{.c1}

[metrics: metric ]{.c1}

[function: function ]{.c1}

[period: period ]{.c1}

[get vm one metric ip\_address\_graphite: ip address graphite pod: pod
name ]{.c1}

[vm: vm name ]{.c1}

[metrics: metric ]{.c1}

[function: function ]{.c1}

[period: period ]{.c1}

[platform k8s   (k8s management) ]{.c2}

[platform k8s app-add add k8s app -C, \--cluster: k8s cluster reference
label -N, \--namespace: k8s current namespace ]{.c1}

[app: app name ]{.c1}

[platform k8s app-del delete k8s app -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[app: app name ]{.c1}

[platform k8s app-get query k8s app -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[app: app name ]{.c1}

[platform k8s cluster-health get cluster health ]{.c1}

[platform k8s cluster-nodes get cluster nodes ]{.c1}

[platform k8s cluster-stats get cluster statistics ]{.c1}

[platform k8s deploy-get get k8s deployment app -C, \--cluster: k8s
cluster reference label -N, \--namespace: k8s current namespace ]{.c1}

[-id: deployment app id ]{.c1}

[platform k8s index-count count index documents -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[index: index name ]{.c1}

[-query: simple query like field1:value1 ]{.c1}

[-sort: sort field. Ex. date:desc\] ]{.c1}

[-fields: comma separated list of fields to show ]{.c1}

[platform k8s index-del delete index index: index name ]{.c1}

[platform k8s index-get get indexes -index: index name -pattern: index
pattern ]{.c1}

[platform k8s index-list list indexes -pattern: index pattern ]{.c1}

[platform k8s index-query query index -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[index: index name ]{.c1}

[-query: simple query like field1:value1 ]{.c1}

[-sort: sort field. Ex. date:desc\] ]{.c1}

[-fields: comma separated list of fields to show ]{.c1}

[platform k8s index-stats get index statistics index: index name
platform k8s info get elastic info ]{.c1}

[platform k8s namespace get ]{.c1}

[get k8s namespace -C, \--cluster: k8s cluster reference label -N,
\--namespace: k8s current namespace]{.c1}

[platform k8s node-get get k8s nodes -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[-id: node id ]{.c1}

[platform k8s ping ping k8s cluster -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[platform k8s pod-connect connect to k8s pod -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[id: pod id ]{.c1}

[-cmd: command to run ]{.c1}

[platform k8s pod-elk-log count ]{.c1}

[get k8s pod elk log count -C, \--cluster: k8s cluster reference label
-N, \--namespace: k8s current namespace ]{.c1}

[-id: pod id ]{.c1}

[platform k8s pod-get get k8s pod -C, \--cluster: k8s cluster reference
label -N, \--namespace: k8s current namespace ]{.c1}

[-id: pod id ]{.c1}

[platform k8s pod-log get k8s pod -C, \--cluster: k8s cluster reference
label -N, \--namespace: k8s current namespace ]{.c1}

[-name: pod name like ]{.c1}

[-id: pod id ]{.c1}

[-lines: the number of lines from the end of the logs to show ]{.c1}

[-follow: follow the log stream of the pod ]{.c1}

[platform k8s role-mapping add ]{.c1}

[platform k8s role-mapping del ]{.c1}

[platform k8s role-mapping get ]{.c1}

[add role mapping name: role mapping name role\_name: role name ]{.c1}

[user\_email: user email ]{.c1}

[realm\_name: realm name ]{.c1}

[delete role mapping name: role mapping name get role mapping -name:
role mapping name ]{.c1}

[platform k8s service-get get k8s service -C, \--cluster: k8s cluster
reference label -N, \--namespace: k8s current namespace ]{.c1}

[platform k8s user-add add user name: user name ]{.c1}

[password: password ]{.c1}

[role: role ]{.c1}

[-full\_name: full\_name ]{.c1}

[-email: full\_name ]{.c1}

[platform k8s user-del delete user name: user name ]{.c1}

[platform k8s user-get get user -name: user name ]{.c1}

[platform kibana   (kibana platform management) ]{.c2}

[platform kibana ping ping kibana -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[platform kibana role-add add role -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[name: role name ]{.c1}

[indice: indice ]{.c1}

[space\_id: space\_id ]{.c1}

[platform kibana role-del delete role -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[name: role name ]{.c1}

[platform kibana role-get get role -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[-name: role name ]{.c1}

[platform kibana space-add add space -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[id: space id]{.c1}

[name: space name ]{.c1}

[-description: space description ]{.c1}

[-color: space color ]{.c1}

[-initials: space initials ]{.c1}

[platform kibana space-del delete space -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[id: space id ]{.c1}

[platform kibana space-get get space -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[-id: space id ]{.c1}

[platform kibana version get kibana version -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: kibana platform reference label ]{.c1}

[platform mysql   (mysql/mariadb management) ]{.c2}

[platform mysql binary-log purge ]{.c1}

[platform mysql binary-log show ]{.c1}

[purge mysql binary logs -O, \--orchestrator: mysql cluster or single
node reference label -port: mysql port ]{.c1}

[show mysql binary logs -O, \--orchestrator: mysql cluster or single
node reference label -port: mysql port ]{.c1}

[platform mysql drop drop mysql db -O, \--orchestrator: mysql cluster or
single node reference label db: db name ]{.c1}

[-port: mysql port ]{.c1}

[platform mysql drops drop mysql dbs -O, \--orchestrator: mysql cluster
or single node reference label dbs: db name comma separated ]{.c1}

[-port: mysql port ]{.c1}

[platform mysql dump dump mysql db -O, \--orchestrator: mysql cluster or
single node reference label db: db name ]{.c1}

[file: dump file ]{.c1}

[platform mysql galera cluster-status ]{.c1}

[get mariadb galera cluster status -O, \--orchestrator: mysql cluster or
single node reference label -port: mysql port ]{.c1}

[-check\_host: list of comma separated host to check ]{.c1}

[platform mysql load load mysql db -O, \--orchestrator: mysql cluster or
single node reference label db: db name ]{.c1}

[file: dump file ]{.c1}

[platform mysql ping ping mysql instance -O, \--orchestrator: mysql
cluster or single node reference label -port: mysql port ]{.c1}

[platform mysql replica slave-start ]{.c1}

[platform mysql replica slave-status ]{.c1}

[platform mysql replica slave-stop ]{.c1}

[start replica on slave -O, \--orchestrator: mysql cluster or single
node reference label -port: mysql port ]{.c1}

[get mariadb slave replica status -O, \--orchestrator: mysql cluster or
single node reference label -port: mysql port ]{.c1}

[stop replica on slave -O, \--orchestrator: mysql cluster or single node
reference label -port: mysql port ]{.c1}

[platform mysql dbs   (mysql database management) ]{.c83}

[platform mysql dbs add add mysql database -O, \--orchestrator: mysql
cluster or single node reference label -port: mysql port ]{.c1}

[name: database name ]{.c1}

[platform mysql dbs drop delete mysql database -O, \--orchestrator:
mysql cluster or single node reference label -port: mysql port ]{.c1}

[name: database name ]{.c1}

[platform mysql dbs get get mysql database list -O, \--orchestrator:
mysql cluster or single node reference label -port: mysql port ]{.c1}

[platform mysql dbusers   (mysql user management) ]{.c83}

[platform mysql dbusers add add mysql user -O, \--orchestrator: mysql
cluster or single node reference label -port: mysql port ]{.c1}

[-host: user host]{.c1}

[platform mysql dbusers drop ]{.c1}

[name: user name ]{.c1}

[pwd: user password ]{.c1}

[delete mysql user -O, \--orchestrator: mysql cluster or single node
reference label -port: mysql port ]{.c1}

[name: user name ]{.c1}

[platform mysql dbusers get get mysql user list -O, \--orchestrator:
mysql cluster or single node reference label -port: mysql port ]{.c1}

[platform mysql dbusers grant ]{.c1}

[grant db to user -O, \--orchestrator: mysql cluster or single node
reference label -port: mysql port ]{.c1}

[-host: user host ]{.c1}

[name: user name ]{.c1}

[-db: db to grant ]{.c1}

[platform mysql tables   (mysql table management) ]{.c83}

[platform mysql tables check check mysql tables -O, \--orchestrator:
mysql cluster or single node reference label db: db name ]{.c1}

[-port: mysql port ]{.c1}

[platform mysql tables desc get mysql table description -O,
\--orchestrator: mysql cluster or single node reference label db: db
name ]{.c1}

[table: table name ]{.c1}

[-port: mysql port ]{.c1}

[platform mysql tables get get mysql table list -O, \--orchestrator:
mysql cluster or single node reference label db: db name ]{.c1}

[-port: mysql port ]{.c1}

[platform mysql tables query query mysql db table -O, \--orchestrator:
mysql cluster or single node reference label db: db name ]{.c1}

[table: table name ]{.c1}

[-rows: query rows number ]{.c1}

[-offset: query rows offset ]{.c1}

[-detail: rotate record output ]{.c1}

[-fields: comma separated list of fields ]{.c1}

[-order: ield used to order records ]{.c1}

[-where: custom where ]{.c1}

[-port: mysql port ]{.c1}

[platform nginx   (Nginx management) ]{.c2}

[platform nginx ping ping nginx instances -O, \--orchestrator: mysql
cluster or single node reference label platform nginx status get nginx
instances status -O, \--orchestrator: mysql cluster or single node
reference label ]{.c1}

[platform ontap   (netapp ontap management) ]{.c2}

[platform ontap cluster-get cluster get -O, \--orchestrator: ontap
platform reference label ]{.c1}

[platform ontap cluster-peer get ]{.c1}

[cluster peer get -O, \--orchestrator: ontap platform reference label
]{.c1}

[platform ontap ping ping ontap -O, \--orchestrator: ontap platform
reference label ]{.c1}

[platform ontap snapmirror get ]{.c1}

[get ontap snapmirror volumes -O, \--orchestrator: ontap platform
reference label -id: svm uuid ]{.c1}

[-source\_path: source path ]{.c1}

[-source\_svm: source svm ]{.c1}

[-dest\_path: dest path ]{.c1}

[platform ontap svm-get get svm -O, \--orchestrator: ontap platform
reference label -id: svm uuid ]{.c1}

[-name: svm name like ]{.c1}

[-order\_by: order by ]{.c1}

[platform ontap svm-peer get ]{.c1}

[svm get peer -O, \--orchestrator: ontap platform reference label -id:
svm uuid ]{.c1}

[-svm: svm name ]{.c1}

[-name: name like ]{.c1}

[-order\_by: order by ]{.c1}

[platform ontap volume-get get volume -O, \--orchestrator: ontap
platform reference label -id: volume uuid ]{.c1}

[-name: volume name like ]{.c1}

[-svm: svm name to limit the search to (volumes \'in that svm\') ]{.c1}

[-H: human readable (i.e. B, KB, MB, GB, TB) ]{.c1}

[-precise: show also size as precise integer multiple of bytes]{.c1}

[platform ontap volume snapshot-get ]{.c1}

[platform ontap volume usage ]{.c1}

[get ontap volume snapshots -O, \--orchestrator: ontap platform
reference label volume: volume uuid ]{.c1}

[get ontap volume usage -O, \--orchestrator: ontap platform reference
label svms: comma separated list of svms ]{.c1}

[-H: human readable (i.e. B, KB, MB, GB, TB) ]{.c1}

[-precise: show also size as precise integer multiple of bytes ]{.c1}

[platform openstack   (openstack platform) ]{.c2}

[platform openstack ]{.c1}

[aggregate-add ]{.c1}

[platform openstack ]{.c1}

[aggregate-del ]{.c1}

[platform openstack ]{.c1}

[aggregate-get ]{.c1}

[platform openstack ]{.c1}

[aggregate-host-add ]{.c1}

[platform openstack ]{.c1}

[aggregate-host-del ]{.c1}

[platform openstack ]{.c1}

[aggregate-metadat-update ]{.c1}

[platform openstack ]{.c1}

[aggregate-update ]{.c1}

[add aggregate -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[name: aggregate name ]{.c1}

[availability\_zone: availability zone ]{.c1}

[delete openstack aggregate -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: aggregate id ]{.c1}

[get aggregates -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: aggregate id ]{.c1}

[add host to openstack aggregate -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: aggregate id ]{.c1}

[host: host\_id ]{.c1}

[delete host from openstack aggregate -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: aggregate id ]{.c1}

[host: host\_id ]{.c1}

[update metadata to openstack aggregate -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: aggregate id ]{.c1}

[metadata: key:value,key:value ]{.c1}

[update openstack aggregate -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: aggregate id ]{.c1}

[-name: aggregate name ]{.c1}

[-availability\_zone: aggregate availability zone ]{.c1}

[platform openstack catalog get openstack keystone catalog -O,
\--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform openstack domain get ]{.c1}

[platform openstack flavor add ]{.c1}

[platform openstack flavor del ]{.c1}

[platform openstack flavor extra-spec-add ]{.c1}

[platform openstack flavor extra-spec-del ]{.c1}

[platform openstack flavor extra-spec-get ]{.c1}

[platform openstack flavor extra-spec-update ]{.c1}

[platform openstack flavor get ]{.c1}

[get domains -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: cluster id ]{.c1}

[add flavor -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[name: flavor name ]{.c1}

[vcpu: vcpu ]{.c1}

[ram: ram ]{.c1}

[disk: disk ]{.c1}

[delete openstack flavor -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[add flavor extra spec -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[spec: flavor extra spec keys. Syntax k1:v1,k2:v2 ]{.c1}

[delete openstack flavor -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[spec: flavor extra spec key ]{.c1}

[get flavor extra specs -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[-spec: flavor extra spec key ]{.c1}

[update openstack flavor -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[spec: flavor extra spec key. Syntax k1:v1 ]{.c1}

[spec\_value: flavor extra spec key ]{.c1}

[get flavors -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: flavor id]{.c1}

[platform openstack flavor update ]{.c1}

[platform openstack ]{.c1}

[floatingip-del ]{.c1}

[platform openstack ]{.c1}

[floatingip-get ]{.c1}

[platform openstack host status ]{.c1}

[platform openstack image add ]{.c1}

[platform openstack image del ]{.c1}

[platform openstack image download ]{.c1}

[platform openstack image get ]{.c1}

[platform openstack image schema-get ]{.c1}

[platform openstack image task-get ]{.c1}

[platform openstack image upload ]{.c1}

[platform openstack keypair del ]{.c1}

[platform openstack keypair get ]{.c1}

[platform openstack ]{.c1}

[keystone-role-get ]{.c1}

[platform openstack ]{.c1}

[keystone-user-get ]{.c1}

[platform openstack ]{.c1}

[mariadb-cluster-status ]{.c1}

[platform openstack ]{.c1}

[mariadb-ping ]{.c1}

[platform openstack ]{.c1}

[network-add ]{.c1}

[platform openstack ]{.c1}

[network-del ]{.c1}

[update openstack flavor -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: flavor id ]{.c1}

[-name: flavor name ]{.c1}

[-desc: flavor description ]{.c1}

[delete openstack floatingip -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: floatingip id ]{.c1}

[get floatingips -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: floatingip id ]{.c1}

[print host status -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-host: node name ]{.c1}

[-loop: if value \> 1 enable query loop ]{.c1}

[add openstack image -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: image name ]{.c1}

[-disk\_format: disk format e.g.: ami, ari, aki, vhd, vhdx, vmdk, raw,
]{.c1}

[qcow2, vdi, ploop, iso ]{.c1}

[-min\_disk: amount of disk space in GB that is required to boot the
]{.c1}

[image. ]{.c1}

[-min\_ram: amount of RAM in MB that is required to boot the image
]{.c1}

[-visibility: image visibility: public, private, shared, or community
]{.c1}

[delete openstack image -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: image id ]{.c1}

[download openstack image -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: image id ]{.c1}

[name: image file name ]{.c1}

[get images -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: image id ]{.c1}

[-owner: owner ]{.c1}

[-visibility: image visibility: all, public, private, shared, or
community ]{.c1}

[get image schemas -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: image id ]{.c1}

[get image tasks -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: image task id ]{.c1}

[upload openstack image -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: image id ]{.c1}

[name: image file name ]{.c1}

[delete openstack keypair -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: keypair id ]{.c1}

[get keypairs -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: keypair id ]{.c1}

[get keystone roles -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get keystone users -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get mariadb galera cluster status -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[ping mariadb instances -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[add openstack network -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: network name ]{.c1}

[project: parent project id ]{.c1}

[-physical\_network: physical network ]{.c1}

[-segmentation\_id: segmentation id ]{.c1}

[-type: network type. Can be flat, vlan, vxlan, or gre ]{.c1}

[-mt: the maximum transmission unit MTU ]{.c1}

[delete openstack network -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: network id]{.c1}

[platform openstack network-get ]{.c1}

[platform openstack network-update ]{.c1}

[get networks -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: network id ]{.c1}

[update openstack network -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: network id ]{.c1}

[-name: network name ]{.c1}

[-shared: network shared ]{.c1}

[-mtu: network mtu ]{.c1}

[platform openstack ping ping openstack -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[platform openstack port add ]{.c1}

[platform openstack port add-batch ]{.c1}

[add openstack port -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: port name ]{.c1}

[network: network id ]{.c1}

[-subnet: subnet id ]{.c1}

[-tenant: tenant id ]{.c1}

[-ipaddress: ip addresses associated to subnet ]{.c1}

[-allowed-ipaddress: allowed ip address ]{.c1}

[-allowed-macaddress: allowed ip macaddress ]{.c1}

[-host: host id ]{.c1}

[-device\_owner: device owner ]{.c1}

[-security\_groups: One or more security group id. ]{.c1}

[add openstack port -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[platform openstack port-del delete openstack port -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[id: port id ]{.c1}

[platform openstack port-get get ports -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[-id: port id ]{.c1}

[-project: project id ]{.c1}

[-network: network id ]{.c1}

[-status: the port status. Value is ACTIVE or DOWN ]{.c1}

[-device: the id of the device that uses this port ]{.c1}

[-device\_owner: the entity type that uses this port. For example: -
]{.c1}

[compute:nova (server instance), network:dhcp (DHCP agent) - ]{.c1}

[network:router\_interface (router interface). ]{.c1}

[-security\_group: the id of any attached security groups ]{.c1}

[platform openstack port update ]{.c1}

[platform openstack project add ]{.c1}

[platform openstack project default-member-set ]{.c1}

[platform openstack project del ]{.c1}

[platform openstack project get ]{.c1}

[platform openstack project member-get ]{.c1}

[platform openstack project quota-get ]{.c1}

[platform openstack project quota-set ]{.c1}

[update openstack port -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: port id ]{.c1}

[-name: port name ]{.c1}

[-desc: port description ]{.c1}

[-sgs: port security groups comma separated ]{.c1}

[-allowed\_ips: a comma separated list of allowed ip address ]{.c1}

[-port\_security\_enabled: enable or disable port security ]{.c1}

[add openstack project -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: project name ]{.c1}

[domain: project domain id ]{.c1}

[-desc: project description ]{.c1}

[-parent: parent project id ]{.c1}

[-enabled: enabled status ]{.c1}

[get openstack project default members -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: project id ]{.c1}

[delete openstack project -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: project id ]{.c1}

[get projects -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[-id: project id ]{.c1}

[get openstack project members -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: project id ]{.c1}

[get project quotas -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: project id ]{.c1}

[set project quotas -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: project id ]{.c1}

[quota\_type: project quota type. can be compute, block, network, share
]{.c1}

[quota: project quota name ]{.c1}

[value: project quota value]{.c1}

[platform openstack project update ]{.c1}

[platform openstack region get ]{.c1}

[platform openstack router add ]{.c1}

[platform openstack router del ]{.c1}

[platform openstack router get ]{.c1}

[platform openstack router port-add ]{.c1}

[platform openstack router port-del ]{.c1}

[platform openstack router reset-routes ]{.c1}

[platform openstack router rewrite-routes ]{.c1}

[platform openstack router update ]{.c1}

[platform openstack ]{.c1}

[security-group-add ]{.c1}

[platform openstack ]{.c1}

[security-group-check ]{.c1}

[platform openstack ]{.c1}

[security-group-del ]{.c1}

[platform openstack ]{.c1}

[security-group-get ]{.c1}

[platform openstack ]{.c1}

[security-group-rule-add ]{.c1}

[platform openstack ]{.c1}

[security-group-rule-del ]{.c1}

[update openstack project -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: project id ]{.c1}

[-name: project name ]{.c1}

[-desc: project description ]{.c1}

[-domain: parent domain id ]{.c1}

[-parent: parent project id ]{.c1}

[-enabled: enabled status ]{.c1}

[get regions -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[add openstack router -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: router name ]{.c1}

[tenant: parent project id ]{.c1}

[-network: physical router ]{.c1}

[-ext-subnet: external subnet ]{.c1}

[-ext-ip: external ip address ]{.c1}

[delete openstack router -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: router id ]{.c1}

[get routers -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: router id ]{.c1}

[add openstack router internal interfafe -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: router id ]{.c1}

[subnet: subnet id ]{.c1}

[-ip: intarface ip ]{.c1}

[delete openstack router internal interfafe -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[id: router id ]{.c1}

[subnet: subnet id ]{.c1}

[reset openstack router routes -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: router id ]{.c1}

[rewrite existing openstack router routes -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: router id ]{.c1}

[update openstack router -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: router id ]{.c1}

[-name: router name ]{.c1}

[-network: physical router ]{.c1}

[-ext-subnet: external subnet ]{.c1}

[-ext-ip: external ip address ]{.c1}

[-routes: routes like dest:nexthop,dest:nexthop ]{.c1}

[add openstack security group -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[name: security\_group name ]{.c1}

[project: parent project id ]{.c1}

[check openstack security\_group -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-delete: security\_group id ]{.c1}

[delete openstack security\_group -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: security\_group id ]{.c1}

[get security\_groups -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: security\_group id ]{.c1}

[add openstack security group rule -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: security group rule id ]{.c1}

[-direction: direction. Can be ingress or egress ]{.c1}

[-ethertype: Must be IPv4 or IPv6 ]{.c1}

[-port\_min: port range min ]{.c1}

[-port\_max: port range max ]{.c1}

[-protocol: protocol ]{.c1}

[-remote\_ip: remote ip ]{.c1}

[delete openstack security group rule -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: security group rule id]{.c1}

[platform openstack ]{.c1}

[security-group-rule-get ]{.c1}

[platform openstack ]{.c1}

[security-group-update ]{.c1}

[platform openstack server action-get ]{.c1}

[platform openstack server add ]{.c1}

[platform openstack server console ]{.c1}

[platform openstack server console-output ]{.c1}

[platform openstack server create-image ]{.c1}

[platform openstack server del ]{.c1}

[platform openstack server diagnostics ]{.c1}

[platform openstack server get ]{.c1}

[platform openstack server group-add ]{.c1}

[platform openstack server group-del ]{.c1}

[platform openstack server group-get ]{.c1}

[platform openstack server group-member-add ]{.c1}

[platform openstack server group-member-del ]{.c1}

[get openstack security group rule -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: security group rule id ]{.c1}

[update openstack security group -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: security\_group id ]{.c1}

[-name: security\_group name ]{.c1}

[-desc: security\_group description ]{.c1}

[get server actions -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[-action: action id ]{.c1}

[add openstack server -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: server name ]{.c1}

[-flavor: flavor reference id ]{.c1}

[-boot\_volume: boot volume id ]{.c1}

[-admin\_pass: admin password ]{.c1}

[-description: description ]{.c1}

[-security\_groups: security groups ]{.c1}

[-networks: list of networks ]{.c1}

[-config\_drive: list of networks ]{.c1}

[-availability\_zone: availability zone ]{.c1}

[-image: The UUID of the image to use for your server instance. ]{.c1}

[get openstack server console -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[get openstack server console output -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server id ]{.c1}

[create image from a server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[name: image name ]{.c1}

[delete openstack server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[get openstack server diagnostics -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server id ]{.c1}

[get servers -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: server id ]{.c1}

[-host: compute node name ]{.c1}

[-status: server status ]{.c1}

[-updated\_at: Filter the server list result by a date and time stamp
]{.c1}

[when the instance was updated. The date and timestamp format is ISO
]{.c1}

[8601: CCYY-MM-DDThh:mm:ss±hh:mm. For example, ]{.c1}

[2015-08-27T09:49:58-05:00 ]{.c1}

[add openstack server group -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[name: server group name ]{.c1}

[-policy: one policy name to associate with the server group. Policy
]{.c1}

[names are: \"anti-affinity\" servers in this group must be scheduled to
]{.c1}

[different hosts, \"affinity\" servers in this group must be scheduled
to ]{.c1}

[the same host, \"soft-anti-affinity\" servers in this group should be
]{.c1}

[scheduled to different hosts if possible, but if not possible then they
]{.c1}

[should still be scheduled instead of resulting in a build failure,
\"soft ]{.c1}

[affinity\" servers in this group should be scheduled to the same host
if ]{.c1}

[possible, but if not possible then they should still be scheduled
instead ]{.c1}

[of resulting in a build failure ]{.c1}

[delete openstack server group -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server group id ]{.c1}

[get server groups -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: server group id ]{.c1}

[-size: number of item to return ]{.c1}

[-page: page to return ]{.c1}

[add openstack server group member -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server group id ]{.c1}

[server: server id ]{.c1}

[delete openstack server group member -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server group id]{.c1}

[platform openstack server lock ]{.c1}

[platform openstack server metadata-add ]{.c1}

[platform openstack server metadata-del ]{.c1}

[platform openstack server metadata-get ]{.c1}

[platform openstack server migrate ]{.c1}

[platform openstack server migration-del ]{.c1}

[platform openstack server migration-list ]{.c1}

[platform openstack server pause ]{.c1}

[platform openstack server port-add ]{.c1}

[platform openstack server port-del ]{.c1}

[platform openstack server port-get ]{.c1}

[platform openstack server reboot ]{.c1}

[platform openstack server rebuild ]{.c1}

[platform openstack server reset-state ]{.c1}

[platform openstack server resize ]{.c1}

[platform openstack server resume ]{.c1}

[platform openstack server sg-add ]{.c1}

[platform openstack server sg-del ]{.c1}

[server: server id ]{.c1}

[lock server -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[add openstack server metadata -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[volume: volume id ]{.c1}

[delete openstack server metadata -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server id ]{.c1}

[volume: volume id ]{.c1}

[get openstack server metadata -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[migrate server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[-host: host id ]{.c1}

[-live: if true enable live migration ]{.c1}

[abort server migration -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[migration\_id: server migration id ]{.c1}

[server migration list -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: server id ]{.c1}

[pause server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[add openstack server port -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[-port: port id ]{.c1}

[-net: network id ]{.c1}

[-ipaddress: ip address ]{.c1}

[-subnet: subnet id ]{.c1}

[delete openstack server port -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[port: port id ]{.c1}

[get openstack server ports -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[reboot server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[rebuild openstack server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[-image: The UUID of the image to use for your server instance. ]{.c1}

[reset server state -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[state: server state ]{.c1}

[set server flavor -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[flavor: flavor id ]{.c1}

[resume server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[add openstack server security group -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server id ]{.c1}

[sg: security group id ]{.c1}

[delete openstack server security group -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: server id ]{.c1}

[sg: security group id ]{.c1}

[platform openstack server- get openstack server security group -O,
\--orchestrator: openstack platform reference label]{.c1}

[sg-get -P, \--project: openstack current project name id: server id
]{.c1}

[platform openstack server smart-ping ]{.c1}

[platform openstack server smart-reset-status ]{.c1}

[platform openstack server smart-start ]{.c1}

[platform openstack server start ]{.c1}

[platform openstack server stop ]{.c1}

[platform openstack server suspend ]{.c1}

[platform openstack server unlock ]{.c1}

[platform openstack server unpause ]{.c1}

[platform openstack server update ]{.c1}

[platform openstack server volume-add ]{.c1}

[platform openstack server volume-del ]{.c1}

[platform openstack server volume-get ]{.c1}

[platform openstack servers migrate ]{.c1}

[platform openstack share add ]{.c1}

[platform openstack share del ]{.c1}

[platform openstack share get ]{.c1}

[platform openstack share grant-add ]{.c1}

[ping servers for a host -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-host: node name ]{.c1}

[-name: vm name ]{.c1}

[reset servers state for a host -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-host: node name ]{.c1}

[start servers for a host -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-host: node name ]{.c1}

[start server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[stop server -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[suspend server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[unlock server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[unpause server -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[update openstack server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[-name: server name ]{.c1}

[-desc: server description ]{.c1}

[add openstack server volume -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[server\_id: server id ]{.c1}

[volume\_id: volume id (see volume-add to create it.) ]{.c1}

[delete openstack server volume -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[volume: volume id ]{.c1}

[get openstack server volumes -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: server id ]{.c1}

[migrate servers -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[from\_host: starting host ]{.c1}

[-to\_host: destination host ]{.c1}

[-live: if true enable live migration ]{.c1}

[add manila share -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: share name ]{.c1}

[size: share size in GB ]{.c1}

[proto: share protocol (NFS, CIFS, GlusterFS, HDFS, or CephFS. ]{.c1}

[CephFS) ]{.c1}

[type: share type id ]{.c1}

[-snapshot: share snapshot id ]{.c1}

[-group: share group id ]{.c1}

[-network: the id of a share network where the share server exists or
]{.c1}

[will be created. If is None and you provide a snapshot\_id, the network
]{.c1}

[value from the snapshot is used ]{.c1}

[delete manila shares -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[-force: if true force delete ]{.c1}

[get manila shares -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: share id ]{.c1}

[add manila share access grant -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[-level: the access level to the share. rw: Read and write (RW) access.
]{.c1}

[ro: Read-only (RO) access. ]{.c1}

[-type: the access rule type. ip: Authenticates an instance through its
IP]{.c1}

[platform openstack share grant-remove ]{.c1}

[platform openstack share limit-get ]{.c1}

[platform openstack share message-get ]{.c1}

[platform openstack share network-add ]{.c1}

[platform openstack share network-del ]{.c1}

[platform openstack share network-get ]{.c1}

[platform openstack share network-security-service add ]{.c1}

[address. cert: Authenticates an instance through a TLS certificate.
]{.c1}

[user: Authenticates by a user or group name. ]{.c1}

[-to: the value that defines the access. ip: A valid format is ]{.c1}

[XX.XX.XX.XX or XX.XX.XX.XX/XX. For example 0.0.0.0/0. cert: Specify
]{.c1}

[the TLS identity as the IDENTKEY. A valid value is any string up to 64
]{.c1}

[characters long in the common name (CN) of the certificate. The ]{.c1}

[meaning of a string depends on its interpretation. user: A valid value
]{.c1}

[is an alphanumeric string that can contain some special characters
]{.c1}

[and is from 4 to 32 characters long. ]{.c1}

[remove manila share access grant -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: share id ]{.c1}

[access\_id: grant id ]{.c1}

[get manila share limits -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[get manila share messages -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: share id ]{.c1}

[add manila share network -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[name: share network name ]{.c1}

[-desc: share network description ]{.c1}

[network: The UUID of a neutron network when setting up or updating
]{.c1}

[a share network subnet with neutron. Specify both a neutron network
]{.c1}

[and a neutron subnet that belongs to that neutron network. ]{.c1}

[subnet: The UUID of the neutron subnet when setting up or updating
]{.c1}

[a share network subnet with neutron. Specify both a neutron network
]{.c1}

[and a neutron subnet that belongs to that neutron network. ]{.c1}

[-availability\_zone: The UUID or name of an availability zone for the
]{.c1}

[share network subnet. ]{.c1}

[delete manila share networks -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share network id ]{.c1}

[get manila share networks -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: share network id ]{.c1}

[-network: neutron network id ]{.c1}

[-subnet: neutron subnet id ]{.c1}

[add security service to share network -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[id: share network id ]{.c1}

[service: security service id ]{.c1}

[platform openstack share network-security-service del ]{.c1}

[delete security service from share network ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name id: share network id ]{.c1}

[service: security service id ]{.c1}

[platform openstack share network-update ]{.c1}

[platform openstack share server-del ]{.c1}

[platform openstack share server-get ]{.c1}

[platform openstack share size-extend ]{.c1}

[platform openstack share size-shrink ]{.c1}

[platform openstack share snapshot-revert ]{.c1}

[update manila share network -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: share network id ]{.c1}

[-name: share network name ]{.c1}

[-desc: share network description ]{.c1}

[-network: The UUID of a neutron network when setting up or updating
]{.c1}

[a share network subnet with neutron. Specify both a neutron network
]{.c1}

[and a neutron subnet that belongs to that neutron network. ]{.c1}

[-subnet: The UUID of the neutron subnet when setting up or updating
]{.c1}

[a share network subnet with neutron. Specify both a neutron network
]{.c1}

[and a neutron subnet that belongs to that neutron network. ]{.c1}

[delete manila share servers -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share server id ]{.c1}

[get manila share servers -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: share server id ]{.c1}

[extend manila share size -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[size: new size of the share, in GBs. ]{.c1}

[shrink manila share size -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[size: new size of the share, in GBs. ]{.c1}

[revert manila share to snapshot -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[snapshot\_id: the share snapshot id]{.c1}

[platform openstack share status-reset ]{.c1}

[platform openstack share type-get ]{.c1}

[platform openstack stack add ]{.c1}

[platform openstack stack del ]{.c1}

[platform openstack stack get ]{.c1}

[platform openstack stack resource-get ]{.c1}

[reset manila share status -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: share id ]{.c1}

[-status: the share access status, which is new, error, active ]{.c1}

[get manila share types -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: share type id ]{.c1}

[-desc: share type description ]{.c1}

[add openstack stack -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: stack name ]{.c1}

[project: parent project id ]{.c1}

[physical\_stack: physical stack ]{.c1}

[-segmentation\_id: segmentation id ]{.c1}

[delete openstack stack -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: stack id ]{.c1}

[get stacks -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: stack id ]{.c1}

[get heat stack resources -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: stack id ]{.c1}

[-resource: stack resource name ]{.c1}

[platform openstack stack resource-patch ]{.c1}

[mark the specified resource in the stack as unhealthy ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name id: stack id ]{.c1}

[-resource: stack resource name ]{.c1}

[platform openstack stack update ]{.c1}

[platform openstack subnet add ]{.c1}

[platform openstack subnet del ]{.c1}

[platform openstack subnet get ]{.c1}

[platform openstack subnet update ]{.c1}

[platform openstack sys-api extension-get ]{.c1}

[platform openstack sys-api get ]{.c1}

[update openstack stack -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: stack id ]{.c1}

[-name: stack name ]{.c1}

[-desc: stack description ]{.c1}

[add openstack subnet -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: subnet name ]{.c1}

[network: parent network id ]{.c1}

[-gateway: gateway ip ]{.c1}

[cidr: subnet cidr ]{.c1}

[-enable-dhcp: enable dhcp ]{.c1}

[dns: comma separated subnet dns ]{.c1}

[delete openstack subnet -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: subnet id ]{.c1}

[get subnets -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: subnet id ]{.c1}

[-project: project id ]{.c1}

[-network: network id ]{.c1}

[update openstack subnet -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: subnet id ]{.c1}

[-name: subnet name ]{.c1}

[-desc: subnet description ]{.c1}

[get api extensions -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get api versions -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[platform openstack sys compute-agent-get ]{.c1}

[get compute agents. Use guest agents to access files on the disk,
configure networking, and run other applications and scripts in the
guest while it runs. This hypervisor-specific extension is not currently
enabled for KVM. Use of guest agents is possible only if the underlying
service provider uses the Xen driver. ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform openstack sys compute-host-aggregate-get ]{.c1}

[platform openstack sys compute-host-get ]{.c1}

[platform openstack sys compute-host-status ]{.c1}

[get compute host aggregates -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[get physical hosts -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[set physical host status -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[host: host id]{.c1}

[platform openstack sys compute-hypervisor-get ]{.c1}

[platform openstack sys compute-hypervisor-servers ]{.c1}

[displays extra statistical information from the machine that hosts the
hypervisor through the API for the hypervisor (XenAPI or KVM/libvirt).
]{.c1}

[displays extra statistical information from the machine that hosts the
hypervisor through the API for the hypervisor (XenAPI or KVM/libvirt).
]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform openstack sys compute-hypervisor-stats ]{.c1}

[platform openstack sys compute-service-get ]{.c1}

[platform openstack sys compute-zone-get ]{.c1}

[platform openstack sys network-agent-get ]{.c1}

[platform openstack sys network-service-provider get ]{.c1}

[platform openstack sys orchestrator-service-get ]{.c1}

[platform openstack sys storage-backend-capabilitie ]{.c1}

[platform openstack sys storage-backend-storage pool-get ]{.c1}

[compute hypervisors statistics -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[get compute services -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get compute availability zones -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[get network agents -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get api versions -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get heat services -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[shows capabilities for a storage back end -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[host: host id ]{.c1}

[lists all back-end storage pools -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[platform openstack sys storage-host-get ]{.c1}

[lists all hosts summary info that is not disabled ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform openstack sys storage-service-get ]{.c1}

[platform openstack sys user-get ]{.c1}

[platform openstack ultra ping ]{.c1}

[get storage service. -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[get users -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[ultra ping openstack -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-vip: if true check only the vip ]{.c1}

[platform openstack ultra ping2 ]{.c1}

[platform openstack ultra ping3 ]{.c1}

[ultra ping openstack instances using an heavy query ]{.c1}

[ultra ping openstack instances components ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name -vip: if true check only the vip ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name -vip: if true check only the vip ]{.c1}

[platform openstack version get openstack version -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[platform openstack volume add ]{.c1}

[platform openstack volume api-extensions ]{.c1}

[platform openstack volume attach ]{.c1}

[platform openstack volume attachment-get ]{.c1}

[add volume -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[name: volume name ]{.c1}

[size: volume size in Gb ]{.c1}

[-type: volume type ]{.c1}

[-snapshot\_id: the snapshot id ]{.c1}

[volume api extensions -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[attach volume from server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[instance: instance id ]{.c1}

[mountpoint: instance mountpoint. ex. /dev/vda ]{.c1}

[get volume attachments -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: volume id ]{.c1}

[-instance: instance id ]{.c1}

[platform openstack volume backend-get ]{.c1}

[get all back-end storage pools that are known to the scheduler service
]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name -hostname: backend storage pool hostname
-backendname: volume backend name ]{.c1}

[platform openstack volume bootable-status-update ]{.c1}

[update volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[-bootable: bootable status ]{.c1}

[platform openstack volume- clone volume -O, \--orchestrator: openstack
platform reference label]{.c1}

[clone -P, \--project: openstack current project name name: volume name
]{.c1}

[volume: volume id ]{.c1}

[project: project id ]{.c1}

[-volume\_type: the volume type id ]{.c1}

[platform openstack volume del ]{.c1}

[platform openstack volume detach ]{.c1}

[platform openstack volume extend ]{.c1}

[platform openstack volume get ]{.c1}

[platform openstack volume group-add ]{.c1}

[platform openstack volume group-del ]{.c1}

[platform openstack volume group-get ]{.c1}

[platform openstack volume group-snapshot-add ]{.c1}

[platform openstack volume group-snapshot-del ]{.c1}

[platform openstack volume group-snapshot-get ]{.c1}

[platform openstack volume group-type-add ]{.c1}

[platform openstack volume group-type-del ]{.c1}

[platform openstack volume group-type-get ]{.c1}

[platform openstack volume group-update ]{.c1}

[platform openstack volume image-metadata-add ]{.c1}

[platform openstack volume image-metadata-del ]{.c1}

[delete volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[-force: force delete ]{.c1}

[detach volume from server -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[extend volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[size: new volume size ]{.c1}

[get volumes -O, \--orchestrator: openstack platform reference label -P,
\--project: openstack current project name ]{.c1}

[-id: volume id ]{.c1}

[-limit: requests a page size of items. Use -1 to list all the volume
]{.c1}

[-offset: used in conjunction with limit to return a slice of items.
offset ]{.c1}

[is where to start in the list ]{.c1}

[add volume group -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: volume group name ]{.c1}

[-availability\_zone: volume group availability zone ]{.c1}

[volume\_types: the list of volume types. In an environment with ]{.c1}

[multiple-storage back ends, the scheduler determines where to send
]{.c1}

[the volume based on the volume type. ]{.c1}

[group\_type: group type id ]{.c1}

[delete volume group -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: volume group id ]{.c1}

[get volume groups -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: volume group id ]{.c1}

[add volume group snapshot -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[group: volume group id ]{.c1}

[-name: volume group snapshot name ]{.c1}

[-desc: volume group snapshot description ]{.c1}

[delete volume group snapshot -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: volume group snapshot id ]{.c1}

[get volume group snapshots -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: volume group snapshot id ]{.c1}

[-group: volume group id ]{.c1}

[add volume group type -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: volume group type name ]{.c1}

[-group\_specs: volume group type specs ]{.c1}

[delete volume group type -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: volume group type id ]{.c1}

[get volume group types -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[-id: volume group id ]{.c1}

[update volume group -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: volume group id ]{.c1}

[-name: volume group name ]{.c1}

[-desc: volume group availability zone ]{.c1}

[-del: One or more volume UUIDs, separated by commas, that you want
]{.c1}

[to remove from group ]{.c1}

[-add: One or more volume UUIDs, separated by commas, that you ]{.c1}

[want to add to group ]{.c1}

[add volume image metadata -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id ]{.c1}

[metadata: key:value string metadata ]{.c1}

[del volume image metadata -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id]{.c1}

[platform openstack volume manage ]{.c1}

[platform openstack volume message-get ]{.c1}

[platform openstack volume metadata-add ]{.c1}

[platform openstack volume metadata-del ]{.c1}

[platform openstack volume migrate ]{.c1}

[platform openstack volume snapshot-add ]{.c1}

[platform openstack volume snapshot-del ]{.c1}

[platform openstack volume snapshot-get ]{.c1}

[platform openstack volume snapshot-revert ]{.c1}

[platform openstack volume snapshot-status-set ]{.c1}

[platform openstack volume status-set ]{.c1}

[platform openstack volume type-get ]{.c1}

[platform openstack volume type-update ]{.c1}

[platform openstack volume unmanage ]{.c1}

[platform openstack volume update ]{.c1}

[metadata: metadata key ]{.c1}

[manage volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[source\_volume\_id: source volume id ]{.c1}

[name: new volume name ]{.c1}

[-desc: new volume description ]{.c1}

[volume\_type: volume type id ]{.c1}

[-bootable: bootable value ]{.c1}

[-host: source volume host ]{.c1}

[-cluster: source volume cluster ]{.c1}

[get volume messages -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: volume message id ]{.c1}

[add volume metadata -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id ]{.c1}

[metadata: key:value string metadata ]{.c1}

[del volume metadata -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id ]{.c1}

[metadata: metadata key ]{.c1}

[migrate volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[volume\_id: volume id ]{.c1}

[host: host ]{.c1}

[-force\_host\_copy: force\_host\_copy ]{.c1}

[-lock\_volume: lock\_volume ]{.c1}

[add volume snapshots -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[name: snapshot name ]{.c1}

[volume: volume id ]{.c1}

[-desc: snapshot description ]{.c1}

[-force: indicates whether to snapshot, even if the volume is attached
]{.c1}

[delete volume snapshot -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id ]{.c1}

[get volume snapshots -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: snapshot id ]{.c1}

[-volume: volume id ]{.c1}

[-group\_snapshot: group snapshot id ]{.c1}

[revert volume to snapshot -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[volume: volume id ]{.c1}

[snapshot: snapshot id ]{.c1}

[set volume snapshot status -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[id: snapshot id ]{.c1}

[-status: snapshot status ]{.c1}

[set volume status -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[-status: volume id ]{.c1}

[get volume types -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[-id: volume type id ]{.c1}

[change volume type -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[volume\_type: volume type id ]{.c1}

[unmanage volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[update volume -O, \--orchestrator: openstack platform reference label
-P, \--project: openstack current project name ]{.c1}

[id: volume id ]{.c1}

[-name: volume name ]{.c1}

[platform redis   (redis management) ]{.c2}

[platform redis cache-del delete cache item -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number]{.c1}

[-port: redis port ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[platform redis cache-get get cache -O, \--orchestrator: redis cluster
or single node reference label -D, \--database: redis database number
]{.c1}

[-port: redis port ]{.c1}

[-db: redis db \[default=0\] ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[-cursor: cursor \[default=0\] ]{.c1}

[-count: count \[default=10\] ]{.c1}

[-value: if True show cache value ]{.c1}

[platform redis client-list client list of redis instances -O,
\--orchestrator: redis cluster or single node reference label -D,
\--database: redis database number ]{.c1}

[-port: redis port ]{.c1}

[platform redis confs config of redis instances -O, \--orchestrator:
redis cluster or single node reference label -D, \--database: redis
database number ]{.c1}

[-port: redis port ]{.c1}

[platform redis delete delete redis records -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[platform redis deletes delete redis keys older than a value in seconds
]{.c1}

[-O, \--orchestrator: redis cluster or single node reference label -D,
\--database: redis database number ]{.c1}

[seconds: min ttl accepted ]{.c1}

[-port: redis port ]{.c1}

[-db: redis db \[default=0\] ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[-cursor: cursor \[default=0\] ]{.c1}

[-count: cursor \[default=10\] ]{.c1}

[platform redis flush flush redis instances -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port ]{.c1}

[platform redis get get redis records by pattern -O, \--orchestrator:
redis cluster or single node reference label -D, \--database: redis
database number ]{.c1}

[-port: redis port ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[platform redis info info from redis instances -O, \--orchestrator:
redis cluster or single node reference label -D, \--database: redis
database number ]{.c1}

[-port: redis port ]{.c1}

[platform redis inspect inspect redis instances -O, \--orchestrator:
redis cluster or single node reference label -D, \--database: redis
database number ]{.c1}

[-port: redis port ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[platform redis ping ping redis instances -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port ]{.c1}

[platform redis scan scan redis instances -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port ]{.c1}

[-db: redis db \[default=0\] ]{.c1}

[-pattern: keys search pattern \[default=\*\] ]{.c1}

[-cursor: cursor \[default=0\] ]{.c1}

[-count: cursor \[default=10\] ]{.c1}

[platform redis sentinel-ping ping redis sentinel instances -O,
\--orchestrator: redis cluster or single node reference label -D,
\--database: redis database number ]{.c1}

[-port: redis port ]{.c1}

[platform redis sentinel status ]{.c1}

[discover redis sentinel status -O, \--orchestrator: redis cluster or
single node reference label -D, \--database: redis database number
]{.c1}

[-port: redis port ]{.c1}

[platform redis set set redis record -O, \--orchestrator: redis cluster
or single node reference label -D, \--database: redis database number
]{.c1}

[-port: redis port ]{.c1}

[key: record key ]{.c1}

[value: record value ]{.c1}

[platform redis size size of redis instances -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port ]{.c1}

[platform redis summary summary of redis instances -O, \--orchestrator:
redis cluster or single node reference label -D, \--database: redis
database number ]{.c1}

[-port: redis port ]{.c1}

[platform redis test test redis cluster -O, \--orchestrator: redis
cluster or single node reference label -D, \--database: redis database
number ]{.c1}

[-port: redis port]{.c1}

[platform scheduler schedules   (cmp scheduler schedule management)
]{.c83}

[platform scheduler schedules add ]{.c1}

[create schedule reading data from a json file ]{.c1}

[-size: list page size \[default=20\] -page: list page \[default=0\]
]{.c1}

[-field: list sort field \[default=id\] -order: list sort order
\[default=DESC\] subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[schedule: schedule config in json file ]{.c1}

[platform scheduler schedules delete ]{.c1}

[platform scheduler schedules get ]{.c1}

[delete schedule by name -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[schedule: schedule name ]{.c1}

[get schedules -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[-name: schedule name ]{.c1}

[platform scheduler tasks   (cmp scheduler task management) ]{.c83}

[platform scheduler tasks definitions ]{.c1}

[platform scheduler tasks get ]{.c1}

[platform scheduler tasks log ]{.c1}

[platform scheduler tasks status ]{.c1}

[platform scheduler tasks test ]{.c1}

[platform scheduler tasks test2 ]{.c1}

[platform scheduler tasks trace ]{.c1}

[list all available tasks you can invoke subsystem: cmp subsystem
\--entity: cmp entity class ]{.c1}

[get task instances -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[-id: task uuid ]{.c1}

[-objid: task entity objid ]{.c1}

[-trace: task entity objid ]{.c1}

[show log for worker instances -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[task: task uuid ]{.c1}

[-index: index name ]{.c1}

[-sort: sort field. Ex. date:desc ]{.c1}

[-pretty: if true show pretty logs ]{.c1}

[-server: server ip ]{.c1}

[get task instance status -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[task: task uuid ]{.c1}

[run test task -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[-number: number of iteration to run ]{.c1}

[-concurrent: number of concurrent task to run ]{.c1}

[run test scheduled action -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[get task instance execution trace -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[task: task uuid ]{.c1}

[platform scheduler tasks tree ]{.c1}

[display list of related tasks in tree-like format ]{.c1}

[-size: list page size \[default=20\] -page: list page
\[default=0\]]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[subsystem: cmp subsystem ]{.c1}

[\--entity: cmp entity class ]{.c1}

[id: task uuid ]{.c1}

[-v: verbose, if true print task steps as well ]{.c1}

[platform trilio   (trilio platform) ]{.c2}

[platform trilio auditlog get auditlog of workload manager -O,
\--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[-time\_in\_minutes: time in minutes(default is 24 hrs.) ]{.c1}

[-time\_from: From date time in format MM-DD-YYYY ]{.c1}

[-time\_to: To date time in format MM-DD-YYYY (default is current day)
]{.c1}

[platform trilio license-add add license -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[license\_file: license file name ]{.c1}

[platform trilio license-check check license -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[platform trilio license-get list license -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[platform trilio protected vm-get ]{.c1}

[platform trilio restore cancel ]{.c1}

[platform trilio restore delete ]{.c1}

[platform trilio restore follow ]{.c1}

[get protected vm -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[cancel the shapshot restore -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[restore: unique identifier of trilio workload snapshot restore ]{.c1}

[delete the shapshot restore -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[restore: unique identifier of trilio workload snapshot restore ]{.c1}

[follow the execution of a shapshot restore -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[restore: unique identifier of trilio workload snapshot restore ]{.c1}

[platform trilio restore-get display the snapshot restore -O,
\--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[-snapshot: snapshot id ]{.c1}

[-id: snapshot restore id ]{.c1}

[platform trilio restore server ]{.c1}

[restore a server from a snapshot. Project with -P must be specified
]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name snapshot: unique identifier of trilio
workload snapshot server: server id ]{.c1}

[-server\_name: server name \[default=-restore-\<..\>\] -overwrite: if
True overwrite server ]{.c1}

[-name: restore name ]{.c1}

[-desc: restore description ]{.c1}

[-network: target : ]{.c1}

[-keep\_ip: keep original ip ]{.c1}

[platform trilio restore volume ]{.c1}

[restore a volume from a snapshot -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[snapshot: unique identifier of trilio workload snapshot ]{.c1}

[volume: volume id ]{.c1}

[-restore\_name: restore name ]{.c1}

[-restore\_desc: restore description ]{.c1}

[platform trilio snapshot-add add a snapshot. Project with -P must be
specified ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name workload: workload id ]{.c1}

[-name: snapshot name ]{.c1}

[-desc: snapshot description ]{.c1}

[-full: snapshot full flag.If True make a full snapshot ]{.c1}

[platform trilio snapshot cancel ]{.c1}

[cancel a snapshot that is running. If the snapshot operation is in the
middle of the data transfer of a resource, it waits for the data
transfer operation is complete before terminating the snapshot
operation. ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name snapshot: snapshot id ]{.c1}

[platform trilio snapshot-del delete a snapshot -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[snapshot: snapshot id ]{.c1}

[platform trilio snapshot-get display the snapshots of the specified
workload ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[-workload: workload id ]{.c1}

[-id: snapshot id ]{.c1}

[-date\_from: From date in format \'YYYY-MM-DDTHH:MM:SS\' eg
2016-10-10T00:00:00, If don\'t specify time then it takes 00:00 by
default \[default=3 day ago\]]{.c1}

[platform trilio snapshot mount ]{.c1}

[platform trilio snapshot mounted ]{.c1}

[platform trilio snapshot umount ]{.c1}

[-date\_to: To date in format \'YYYY-MM-DDTHH:MM:SS\', Specify ]{.c1}

[HH:MM:SS to get snapshots within same day inclusive/exclusive ]{.c1}

[results for date\_from and date\_to \[default=today\] ]{.c1}

[mount a snapshot to an instance -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[snapshot: snapshot id ]{.c1}

[instance: instance id where mount snapshot ]{.c1}

[list of all mounted snapshots -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[umount a snapshot from an instance -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[snapshot: snapshot id ]{.c1}

[platform trilio status Return the status ( true or false ) of the Cloud
Wide TrilioVault Job Scheduler ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform trilio storage usage ]{.c1}

[get workload storage usage -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[platform trilio tenant-usage Gives storage used and vms protected by
tenants ]{.c1}

[platform trilio workload-add add a workload. Project with -P must be
specified ]{.c1}

[platform trilio workload-del delete the workload. Project with -P must
be specified ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name name: workload name ]{.c1}

[type\_id: workload type id ]{.c1}

[instances: comme separated list of instances -metadata: metadata ]{.c1}

[-desc: workload description ]{.c1}

[-fullbackup\_interval: fullbackup interval \[default=2\] -start\_date:
start date. Ex. \'06/05/2014\' ]{.c1}

[-end\_date: end date. Ex. \'07/15/2014\' ]{.c1}

[-start\_time: start time. Ex. \'2:30 PM\' \[default=\'4:00 AM\'\]
-interval: interval. \[default=24hrs\] ]{.c1}

[-snapshots\_to\_retain: snapshots to retain \[default=4\] -timezone:
timezone \[default=Europe/Rome\] ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name workload: workload id ]{.c1}

[platform trilio workload-get get workload -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[-id: workload id ]{.c1}

[-verbose: workload verbose info ]{.c1}

[platform trilio workload reset ]{.c1}

[platform trilio workload status ]{.c1}

[Reset the workload. TrilioVault uses storage based snapshots for
calculating backup images of application resources. For cinder volumes,
it uses cinder snapshots and for ceph based nova backends, it uses ceph
snapshots for calculating the backup images. ]{.c1}

[Depending the state of the workload backup operation, each of these
resources may have one or more snapshots outstanding. Workload-reset
deletes all outstanding snapshots on all resources of the application.
Workload-reset is useful if you want to decommission the ]{.c1}

[application, but you still want to keep all the backups of the
application. NOTE: It is highly recommended to perform workload-reset
before deleting any application resources from OpenStack. ]{.c1}

[display workloads status with the last snapshot ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name workload: workload id ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[platform trilio workload types ]{.c1}

[platform trilio workload unlock ]{.c1}

[display workload types -O, \--orchestrator: openstack platform
reference label -P, \--project: openstack current project name ]{.c1}

[unlock the workload -O, \--orchestrator: openstack platform reference
label -P, \--project: openstack current project name ]{.c1}

[workload: workload id ]{.c1}

[platform trilio workload update ]{.c1}

[update the workload. Project with -P must be specified ]{.c1}

[-O, \--orchestrator: openstack platform reference label -P, \--project:
openstack current project name workload: workload id ]{.c1}

[-name: workload name ]{.c1}

[-instances: comme separated list of instances -metadata: metadata
]{.c1}

[-desc: workload description ]{.c1}

[-fullbackup\_interval: fullbackup interval ]{.c1}

[-start\_date: start date. Ex. \'06/05/2014\' ]{.c1}

[-end\_date: end date. Ex. \'07/15/2014\' ]{.c1}

[-start\_time: start time. Ex. \'2:30 PM\' ]{.c1}

[-interval: interval]{.c1}

[-snapshots\_to\_retain: snapshots to retain ]{.c1}

[-timezone: timezone ]{.c1}

[-enabled: enable workloa ]{.c1}

[platform veeam   (veeam platform management) ]{.c2}

[platform veeam backup-get get backup -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: veeam platform reference label ]{.c1}

[-job\_id: job uid ]{.c1}

[-uid: backup uid ]{.c1}

[-name: backup name pattern (es. \*BCK\*) ]{.c1}

[platform veeam job-get get job -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: veeam platform reference label ]{.c1}

[-uid: job uid ]{.c1}

[-name: job name pattern (es. \*BCK\*) ]{.c1}

[platform veeam ping ping veeam -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: veeam platform reference label ]{.c1}

[platform veeam restorepoint-get ]{.c1}

[get restorepoint -size: list page size \[default=20\] -page: list page
\[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: veeam platform reference label ]{.c1}

[-backup\_id: backup uid ]{.c1}

[-uid: restorepoint uid ]{.c1}

[-name: restorepoint name pattern (es. \*centos\*) ]{.c1}

[platform veeam version get veeam version -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-O, \--orchestrator: veeam platform reference label ]{.c1}

[platform virsh   (libvirt platform) ]{.c2}

[platform virsh domain-get get libvirt host domains -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[hostip: host ip ]{.c1}

[-status: domain status can be: 1 - ACTIVE, 2 - INACTIVE, 4 - ]{.c1}

[PERSISTENT, 8 - TRANSIENT, 16 - RUNNING, 32 - PAUSED, 64 - ]{.c1}

[SHUTOFF, 128 - OTHER ]{.c1}

[-id: domain name ]{.c1}

[platform virsh domain-ping ping libvirt host domains -O,
\--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[hostip: host ip ]{.c1}

[-id: domain name ]{.c1}

[platform virsh domain-stats get libvirt host domain stats -O,
\--orchestrator: openstack platform reference label -P, \--project:
openstack current project name ]{.c1}

[hostip: host ip ]{.c1}

[-id: domain name ]{.c1}

[platform virsh domain usage ]{.c1}

[get libvirt host domain usage date -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[hostip: host ip ]{.c1}

[-id: domain name ]{.c1}

[platform virsh hosts get libvirt hosts -O, \--orchestrator: openstack
platform reference label -P, \--project: openstack current project name
]{.c1}

[platform virsh servers get libvirt host domains -O, \--orchestrator:
openstack platform reference label -P, \--project: openstack current
project name ]{.c1}

[hostip: host ip ]{.c1}

[-status: domain status can be: 1 - ACTIVE, 2 - INACTIVE, 4 - ]{.c1}

[PERSISTENT, 8 - TRANSIENT, 16 - RUNNING, 32 - PAUSED, 64 - ]{.c1}

[SHUTOFF, 128 - OTHER ]{.c1}

[platform vsphere   (vsphere platform)]{.c2}

[platform vsphere cluster get ]{.c1}

[platform vsphere ]{.c1}

[datacenter-get ]{.c1}

[platform vsphere ]{.c1}

[datacenter-sessions ]{.c1}

[platform vsphere datastore get ]{.c1}

[get clusters -O, \--orchestrator: vsphere platform reference label -P,
\--project: vsphere current project name ]{.c1}

[-id: cluster id ]{.c1}

[get datacenters -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[-id: cluster id ]{.c1}

[get datacenter sessions -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[get datastores -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[-id: datastore id ]{.c1}

[platform vsphere dfw exclusion-add ]{.c1}

[platform vsphere dfw exclusion-del ]{.c1}

[add member to distributed firewall exclusion list ]{.c1}

[delete member from distributed firewall exclusion list ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name member: member id ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name member: member id ]{.c1}

[platform vsphere dfw exclusion-get ]{.c1}

[platform vsphere dfw-rule add ]{.c1}

[platform vsphere dfw-rule get ]{.c1}

[platform vsphere dfw-rules del ]{.c1}

[platform vsphere dfw section-add ]{.c1}

[platform vsphere dfw section-check ]{.c1}

[platform vsphere dfw section-del ]{.c1}

[platform vsphere dfw section-get ]{.c1}

[get distributed firewall exclusion list -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[add distributed firewall rule -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[section: section id ]{.c1}

[name: rule name ]{.c1}

[-action: rule action: allow or deny ]{.c1}

[-direction: rule name ]{.c1}

[-sources: rule sources. Ex. SecurityGroup:securitygroup ]{.c1}

[22,Ipv4Address:10.1.1.0/24 ]{.c1}

[-dests: rule sources. Ex. SecurityGroup:securitygroup ]{.c1}

[22,Ipv4Address:10.1.1.0/24 ]{.c1}

[-services: rule services ]{.c1}

[-appliedto: rule sources. Ex. ]{.c1}

[DISTRIBUTED\_FIREWALL:DISTRIBUTED\_FIREWALL ]{.c1}

[get distributed firewall rules -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[section: section id ]{.c1}

[rule: rule id ]{.c1}

[delete distributed firewall rules -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[section: section id ]{.c1}

[rules: comma separated list of rules id ]{.c1}

[add distributed firewall sections -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[name: section name ]{.c1}

[check distributed firewall sections -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[delete distributed firewall sections -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[section: section id ]{.c1}

[get distributed firewall sections -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[-id: section id ]{.c1}

[platform vsphere dfw-status get distributed firewall status -O,
\--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name ]{.c1}

[-section: section id ]{.c1}

[platform vsphere dlr-get list vsphere dlr -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[platform vsphere dvpg-add add vsphere dvpg -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[name: dvpg name ]{.c1}

[vlan: dvpg vlan ]{.c1}

[dvs: dvpg dvs ]{.c1}

[platform vsphere dvpg-del delete vsphere dvpg -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: dvpg id ]{.c1}

[platform vsphere dvpg-get get dvpgs -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: dvpg id]{.c1}

[platform vsphere dvs-get get dvss -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[-id: dvs id ]{.c1}

[platform vsphere edge-add add vsphere edge -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[name: edge name ]{.c1}

[datacenter: datacenter mor-id ]{.c1}

[cluster: cluster mor-id ]{.c1}

[datastore: datastore mor-id ]{.c1}

[uplink\_dvpg: uplink dvpg mor-id ]{.c1}

[uplink\_ipaddress: uplink address ]{.c1}

[uplink\_prefix: uplink prefix ]{.c1}

[pwd: admin user password ]{.c1}

[dns1: dns name server 1 ]{.c1}

[domain: dns zone ]{.c1}

[platform vsphere edge appliance-get ]{.c1}

[platform vsphere edge availability-config ]{.c1}

[get edge appliances -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[-appliance: appliance id ]{.c1}

[delete vsphere edge -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[platform vsphere edge-del delete vsphere edge -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: edge id ]{.c1}

[platform vsphere edge dhcp-config ]{.c1}

[platform vsphere edge-dns config ]{.c1}

[platform vsphere edge-fw config ]{.c1}

[platform vsphere edge-fw rule-add ]{.c1}

[platform vsphere edge-fw rule-del ]{.c1}

[platform vsphere edge-fw rule-get ]{.c1}

[platform vsphere edge-fw rule-update ]{.c1}

[delete vsphere edge -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[delete vsphere edge -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[get edge firewall config -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge firewall rule -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[name: rule name ]{.c1}

[-action: rule action. Can be: accept, deny ]{.c1}

[-direction: rule direction. Can be: in, out ]{.c1}

[-logged: rule logged ]{.c1}

[-desc: rule description ]{.c1}

[-enabled: rule name ]{.c1}

[-source: rule source. list of comma separated item like: ip:, grp:,
vnic: ]{.c1}

[-dest: rule destination. list of comma separated item like: ip:, grp:,
]{.c1}

[vnic: ]{.c1}

[-app: rule application. list of comma separated item like: app:, ]{.c1}

[ser:proto+port+source\_port ]{.c1}

[delete edge firewall rule -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[rule: rule id ]{.c1}

[get edge firewall rule -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[rule: rule id ]{.c1}

[update edge firewall rule -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: rule id ]{.c1}

[-name: rule name ]{.c1}

[-desc: rule description ]{.c1}

[-act: rule action ]{.c1}

[-dir: rule direction ]{.c1}

[-src\_add: add rule source ]{.c1}

[-src\_del: remove rule source ]{.c1}

[-dst\_add: add rule destination ]{.c1}

[-dst\_del: remove rule destination ]{.c1}

[-appl: rule application ]{.c1}

[-logged: enable rule log ]{.c1}

[-enabled: enable rule ]{.c1}

[platform vsphere edge-get get vsphere edges -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[-id: edge id]{.c1}

[platform vsphere edge-gslb config ]{.c1}

[platform vsphere edge ipsec-config ]{.c1}

[platform vsphere edge-job get ]{.c1}

[platform vsphere edge l2vpn-get ]{.c1}

[platform vsphere edge-lb app-profile-add ]{.c1}

[get edge global load balancer config -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[delete vsphere edge -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[get vsphere edge job -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: job id ]{.c1}

[get vsphere edge l2 vpn config -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge load balancer application profile -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[name: profile name ]{.c1}

[template: network traffic template {TCP,UDP,HTTP,HTTPS} ]{.c1}

[-http\_redirect\_url: HTTP redirect URL ]{.c1}

[-persistence: persistence method ]{.c1}

[-expire: persistence time in seconds \[Default=300\] ]{.c1}

[-cookie\_name: cookie name ]{.c1}

[-cookie\_mode: cookie mode \[Default=insert\] ]{.c1}

[-insert\_x\_forwarded\_for: insert X-Forwarded-for HTTP header ]{.c1}

[\[Default=False\] ]{.c1}

[-ssl\_passthrough: enable SSL passthrough \[Default=False\] ]{.c1}

[-client\_ssl\_serv\_cert: client service certificate id. Required when
client ]{.c1}

[ssl=True ]{.c1}

[-client\_ssl\_ca\_cert: client ca certificate id \[Optional\] ]{.c1}

[-client\_ssl\_cipher: client cipher suite \[Default=DEFAULT\] ]{.c1}

[-client\_auth: whether peer certificate should be verified ]{.c1}

[\[Default=Ignore\] ]{.c1}

[-server\_ssl\_serv\_cert: server service certificate id ]{.c1}

[-server\_ssl\_ca\_cert: server ca certificate id. Mandatory if
-server\_auth ]{.c1}

[is set to Required ]{.c1}

[-server\_ssl\_cipher: server cipher suite \[Default=DEFAULT\] ]{.c1}

[-server\_auth: whether peer certificate should be verified ]{.c1}

[\[Default=Ignore\] ]{.c1}

[-server\_ssl\_enabled: enable pool side SSL \[Default=False\] ]{.c1}

[platform vsphere edge-lb app-profile-del ]{.c1}

[platform vsphere edge-lb app-profile-get ]{.c1}

[platform vsphere edge-lb app-profile-update ]{.c1}

[delete edge load balancer application profile ]{.c1}

[get edge load balancer application profiles ]{.c1}

[update edge load balancer application profile ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: profile id ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[-id: application profile id ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: profile id ]{.c1}

[-http\_redirect\_url: HTTP redirect URL ]{.c1}

[-persistence: persistence method ]{.c1}

[-expire: persistence time in seconds \[Default=300\] -cookie\_name:
cookie name ]{.c1}

[-cookie\_mode: cookie mode \[Default=insert\] ]{.c1}

[-insert\_x\_forwarded\_for: insert X-Forwarded-for HTTP header
\[Default=False\] ]{.c1}

[platform vsphere edge-lb config-get ]{.c1}

[get edge load balancer config -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[platform vsphere edge-lb config-set ]{.c1}

[set general edge load balancer parameters ]{.c1}

[-O, \--orchestrator: vsphere platform reference label ]{.c1}

[-P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[-acceleration: force load balancer to use L4 engine which is faster and
more efficient than L7 engine ]{.c1}

[-logging: enable/disable load balancer logging ]{.c1}

[-log\_level: logging level ]{.c1}

[platform vsphere edge-lb monitor-add ]{.c1}

[add edge load balancer monitor -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[name: monitor name ]{.c1}

[type: monitor type {HTTP,HTTPS,TCP,ICMP,UDP} ]{.c1}

[-interval: interval in seconds in which a server is to be tested ]{.c1}

[\[Default=5\] ]{.c1}

[-timeout: maximum time in seconds in which a response from the ]{.c1}

[server must be received \[Default=15\] ]{.c1}

[-max\_retries: maximum number of times the server is tested before it
]{.c1}

[is declared down \[Default=3\] ]{.c1}

[-method: method to send the health check request to the server ]{.c1}

[\[Default=GET for HTTP/HTTPS monitor type\]]{.c1}

[platform vsphere edge-lb monitor-del ]{.c1}

[platform vsphere edge-lb monitor-get ]{.c1}

[-url: URL to GET or POST \[Default=\"/\" for HTTP/HTTPS monitor type\]
]{.c1}

[-expected: expected string \[Default=\"HTTP/1\" for HTTP/HTTPS ]{.c1}

[monitor type\] ]{.c1}

[-send: string to be sent to the backend server after a connection is
]{.c1}

[established. This option is mandatory when monitor type is UDP. ]{.c1}

[-receive: string to be received from the backend server for ]{.c1}

[HTTP/HTTPS protocol. This option is mandatory when monitor type is
]{.c1}

[UDP. ]{.c1}

[-extension: advanced monitor configuration. ]{.c1}

[delete edge load balancer monitor -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: monitor id ]{.c1}

[get edge load balancer monitors -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[-id: monitor id ]{.c1}

[-name: monitor name ]{.c1}

[platform vsphere edge-lb monitor-update ]{.c1}

[update edge load balancer service monitor ]{.c1}

[-O, \--orchestrator: vsphere platform reference label ]{.c1}

[-P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: monitor id ]{.c1}

[-interval: interval in seconds in which a server is to be tested
\[Default=5\] ]{.c1}

[-timeout: maximum time in seconds in which a response from the server
must be received \[Default=15\] ]{.c1}

[-max\_retries: maximum number of times the server is tested before it
is declared down \[Default=3\] ]{.c1}

[-method: method to send the health check request to the server
\[Default=GET for HTTP/HTTPS monitor type\] ]{.c1}

[-url: URL to GET or POST \[Default=\"/\" for HTTP/HTTPS monitor type\]
-expected: expected string \[Default=\"HTTP/1\" for HTTP/HTTPS monitor
type\] ]{.c1}

[-send: string to be sent to the backend server after a connection is
established. This option is mandatory when monitor type is UDP.
-receive: string to be received from the backend server for HTTP/HTTPS
protocol. This option is mandatory when monitor type is UDP. ]{.c1}

[platform vsphere edge-lb pool-add ]{.c1}

[platform vsphere edge-lb pool-del ]{.c1}

[platform vsphere edge-lb pool-get ]{.c1}

[platform vsphere edge-lb pool-member-add ]{.c1}

[add edge load balancer pool -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[name: pool name ]{.c1}

[algorithm: balancing algorithm {round-robin,ip-hash,leastconn,uri}
]{.c1}

[-desc: pool description ]{.c1}

[-transparent: whether client IP addresses are visible to the backend
]{.c1}

[servers ]{.c1}

[-monitor: health check monitor id ]{.c1}

[-ip\_ver: ip address version ]{.c1}

[delete edge load balancer pool -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: pool id ]{.c1}

[get edge load balancer pools -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[-id: pool id ]{.c1}

[-name: pool name ]{.c1}

[add member to edge load balancer pool -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[id: pool id ]{.c1}

[name: member name ]{.c1}

[-ip\_addr: member ip address ]{.c1}

[-grouping\_obj\_id: member grouping object id ]{.c1}

[-port: member port ]{.c1}

[-monit\_port: monitor port ]{.c1}

[-weight: member weight ]{.c1}

[-max\_conn: maximum number of concurrent connections a member ]{.c1}

[can handle. Default is 0 which means unlimited ]{.c1}

[-min\_conn: minimum number of concurrent connections a member can
]{.c1}

[handle. Default is 0 which means unlimited ]{.c1}

[-cond: Whether the member is enabled or disabled. Default is enabled
]{.c1}

[platform vsphere edge-lb pool-members-del ]{.c1}

[remove member from edge load balancer pool ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name edge: edge id ]{.c1}

[pool: pool id ]{.c1}

[ids: comma separated list of member ids ]{.c1}

[platform vsphere edge-lb pool-update ]{.c1}

[update edge load balancer pool -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[id: pool id]{.c1}

[platform vsphere edge-lb rule-add ]{.c1}

[-algorithm: balancing algorithm {round-robin,ip-hash,leastconn,uri}
]{.c1}

[-transparent: whether client IP addresses are visible to the backend
]{.c1}

[servers ]{.c1}

[add edge load balancer application rule -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[name: rule name ]{.c1}

[script: rule script. If it starts with \"@\", read content from a file.
E.g. ]{.c1}

[acl is\_site01 hdr\_dom(host) -i test-lb.site01.nivolapiemonte.it \|
]{.c1}

[use\_backend test-pool-1 if is\_site01 ]{.c1}

[platform vsphere edge-lb rule-del ]{.c1}

[delete edge load balancer application rules ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name edge: edge id ]{.c1}

[id: rule id ]{.c1}

[platform vsphere edge-lb rule-get ]{.c1}

[get edge load balancer application rules -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[-id: rule id ]{.c1}

[platform vsphere edge-lb rule-update ]{.c1}

[update edge load balancer application rules ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name edge: edge id ]{.c1}

[id: rule id ]{.c1}

[-name: rule name ]{.c1}

[-script: rule script ]{.c1}

[platform vsphere edge-lb start ]{.c1}

[platform vsphere edge-lb stats-get ]{.c1}

[platform vsphere edge-lb stop ]{.c1}

[platform vsphere edge-lb virt-server-add ]{.c1}

[enable edge load balancer -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[get edge load balancer statistics -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[-pool: pool id ]{.c1}

[disable edge load balancer -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[edge: edge id ]{.c1}

[add edge load balancer virtual server -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[name: virtual server name ]{.c1}

[ip\_address: ip address that the load balancer is listening on ]{.c1}

[protocol: virtual server protocol {HTTP,HTTPS} ]{.c1}

[port: port number ]{.c1}

[app\_profile: application profile id ]{.c1}

[pool: pool id ]{.c1}

[-desc: virtual server description ]{.c1}

[-max\_conn: maximum concurrent connections ]{.c1}

[-max\_conn\_rate: maximum incoming new connection requests per ]{.c1}

[second ]{.c1}

[-acceleration\_enabled: use faster L4 load balancer engine rather than
]{.c1}

[L7 load balancer engine ]{.c1}

[platform vsphere edge-lb virt-server-add-account desc ]{.c1}

[Add account in description of nsx virtual server ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name edge: edge id ]{.c1}

[-id: virtual server id ]{.c1}

[platform vsphere edge-lb virt-server-del ]{.c1}

[platform vsphere edge-lb virt-server-disable ]{.c1}

[platform vsphere edge-lb virt-server-enable ]{.c1}

[platform vsphere edge-lb virt-server-get ]{.c1}

[platform vsphere edge-lb virt-server-update ]{.c1}

[delete edge load balancer virtual server -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[id: virtual server id ]{.c1}

[disable edge load balancer virtual server -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[id: virtual server id ]{.c1}

[enable edge load balancer virtual server -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[id: virtual server id ]{.c1}

[get edge load balancer virtual servers -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[-id: virtual server id ]{.c1}

[update edge load balancer virtual server -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[edge: edge id ]{.c1}

[id: virtual server id ]{.c1}

[-enabled: whether the virtual server is enabled ]{.c1}

[-ip\_address: ip address that the load balancer is listening on ]{.c1}

[-protocol: virtual server protocol]{.c1}

[platform vsphere edge-nat config ]{.c1}

[platform vsphere edge-nat rule-add ]{.c1}

[platform vsphere edge-nat rule-del ]{.c1}

[platform vsphere edge route-default-add ]{.c1}

[platform vsphere edge route-del-all ]{.c1}

[platform vsphere edge route-get ]{.c1}

[platform vsphere edge route-static-add ]{.c1}

[platform vsphere edge route-static-get ]{.c1}

[platform vsphere edge-set pwd ]{.c1}

[platform vsphere edge sslvpn-delete ]{.c1}

[platform vsphere edge sslvpn-disable ]{.c1}

[platform vsphere edge sslvpn-enable ]{.c1}

[platform vsphere edge sslvpn-get ]{.c1}

[platform vsphere edge sslvpn-install-pkg-add ]{.c1}

[platform vsphere edge sslvpn-install-pkg-del ]{.c1}

[-port: port number ]{.c1}

[-app\_profile: application profile id ]{.c1}

[-pool: pool id ]{.c1}

[get edge nat config -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge nat rule -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[desc: rule description ]{.c1}

[action: can be dnat, snat ]{.c1}

[original\_address: original address ]{.c1}

[translated\_address: translated address ]{.c1}

[-logged: if True enable logging ]{.c1}

[-enabled: if True enable nat ]{.c1}

[-original\_port: original port ]{.c1}

[-translated\_port: translated port ]{.c1}

[-protocol: protocol ]{.c1}

[-vnic: vnic ]{.c1}

[delete edge nat rule -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[rule: rule id ]{.c1}

[add edge default route -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[gateway: edge gateway ]{.c1}

[-mtu: mtu ]{.c1}

[-vnic: vnic ]{.c1}

[delete edge static route -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[get edge routing info -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge static route -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[desc: rule description ]{.c1}

[network: network ]{.c1}

[next\_hop: next\_hop address ]{.c1}

[-mtu: mtu ]{.c1}

[-vnic: if True enable logging ]{.c1}

[get edge static routes -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[set vsphere edge admin password -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[pwd: edge admin password ]{.c1}

[delete edge ssl vpn service -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[disable edge ssl vpn service -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[enable edge ssl vpn service -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[get edge ssl vpn config -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge ssl vpn install pkg -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[name: install package name ]{.c1}

[gateways: comma separated list of gateway. server:port ]{.c1}

[delete all the edge ssl vpn install pkg -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[install\_pkg: install\_pkg id]{.c1}

[platform vsphere edge sslvpn-install-pkg-del-all ]{.c1}

[platform vsphere edge sslvpn-ip-pool-add ]{.c1}

[platform vsphere edge sslvpn-ip-pool-del ]{.c1}

[platform vsphere edge sslvpn-ip-pool-del-all ]{.c1}

[platform vsphere edge sslvpn-private-network-add ]{.c1}

[delete all the edge ssl vpn install pkg -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[add edge ssl vpn ippool -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[-ip\_range: ip range. Default 172.30.0.10-172.30.0.99 ]{.c1}

[-netmask: netmask. Default 255.255.255.0 ]{.c1}

[-gateway: gateway. Default 172.30.0.1 ]{.c1}

[-primary\_dns: primary dns. Default 10.103.48.1 ]{.c1}

[-secondary\_dns: secondary dns. Default 10.103.48.2 ]{.c1}

[-dns\_suffix: dns suffix ]{.c1}

[-wins\_server: wins server ]{.c1}

[delete all the edge ssl vpn ippool -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[ippool: ippool id ]{.c1}

[delete all the edge ssl vpn ippool -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[add edge ssl vpn private network -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[network: network cidr ]{.c1}

[-optimize: send tunnel optimize ]{.c1}

[platform vsphere edge sslvpn-private-network-del ]{.c1}

[platform vsphere edge sslvpn-private-network-del all ]{.c1}

[delete all the edge ssl vpn private network ]{.c1}

[delete all the edge ssl vpn private network ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name id: edge id ]{.c1}

[network: network id ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name id: edge id ]{.c1}

[platform vsphere edge sslvpn-server-add ]{.c1}

[platform vsphere edge sslvpn-session-delete ]{.c1}

[platform vsphere edge sslvpn-session-get ]{.c1}

[platform vsphere edge sslvpn-user-add ]{.c1}

[platform vsphere edge sslvpn-user-del ]{.c1}

[platform vsphere edge syslog-add ]{.c1}

[platform vsphere edge syslog-del ]{.c1}

[platform vsphere edge syslog-get ]{.c1}

[platform vsphere edge-vnic add ]{.c1}

[add edge ssl vpn server config -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[ip: server ip address ]{.c1}

[port: server port ]{.c1}

[delete vsphere edge sslvpn session -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: edge id ]{.c1}

[session: edge id ]{.c1}

[get vsphere edge sslvpn sessions -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge ssl vpn user -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[user\_id: user id ]{.c1}

[password: user password ]{.c1}

[first\_name: first name ]{.c1}

[last\_name: last name ]{.c1}

[desc: user description ]{.c1}

[-disable: disable user account ]{.c1}

[-password\_never\_expires: password never expires ]{.c1}

[-change\_password\_on\_next\_login: change password on next login
]{.c1}

[delete all the edge ssl vpn user -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[user: user id ]{.c1}

[add edge syslog servers -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[servers: rsyslog server ip address comma separated ]{.c1}

[delete edge syslog servers -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[get edge syslog config -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[add edge vnic -O, \--orchestrator: vsphere platform reference label -P,
\--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[index: vnic index ]{.c1}

[-type: vnic type. Uplink or Internal ]{.c1}

[portgroup: vnic portgroup id]{.c1}

[platform vsphere edge-vnic del ]{.c1}

[platform vsphere edge-vnic get ]{.c1}

[platform vsphere edge-vnic update ]{.c1}

[ip: vnic primary ip ]{.c1}

[delete edge vnic -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[vnic: vnic index ]{.c1}

[get edge vinics -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[-id: edge id ]{.c1}

[-vnic: vnic id ]{.c1}

[update edge vnic -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[id: edge id ]{.c1}

[vnic: vnic index ]{.c1}

[-secondary\_ip\_add: add sub-interface ]{.c1}

[-secondary\_ip\_del: remove sub-interface ]{.c1}

[platform vsphere folder-add add vsphere folder -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[name: folder name ]{.c1}

[desc: folder description ]{.c1}

[-datacenter: parent datacenter morid ]{.c1}

[-folder: parent folder morid ]{.c1}

[platform vsphere folder-del delete vsphere folder -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: folder id ]{.c1}

[platform vsphere folder-get get folders -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: folder id ]{.c1}

[platform vsphere folder update ]{.c1}

[update vsphere folder -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: folder id ]{.c1}

[-name: folder name ]{.c1}

[-desc: folder description ]{.c1}

[-datacenter: parent datacenter morid ]{.c1}

[-folder: parent folder morid ]{.c1}

[platform vsphere host-get get hosts -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: host id ]{.c1}

[platform vsphere ippool-add add vsphere ippool -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[name: ippool name ]{.c1}

[startip: start ip ]{.c1}

[stopip: stop ip ]{.c1}

[gw: gateway ]{.c1}

[dns1: dns1 ]{.c1}

[dns2: dns2 ]{.c1}

[-prefix: prefix ]{.c1}

[-dnssuffix: dns zone ]{.c1}

[platform vsphere ippool-del delete vsphere ippool -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: ippool id ]{.c1}

[platform vsphere ippool-get get vsphere ippools -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[-id: ippool id ]{.c1}

[-range: ippool range ]{.c1}

[platform vsphere ippool-ip release ]{.c1}

[platform vsphere ippool-ip usage ]{.c1}

[platform vsphere ippool-ip use ]{.c1}

[platform vsphere ippool update ]{.c1}

[release ippool ip -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[id: ippool id ]{.c1}

[ip: ippool ip to use ]{.c1}

[get all allocated ippool ips -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: ippool id ]{.c1}

[assign ippool ip -O, \--orchestrator: vsphere platform reference label
-P, \--project: vsphere current project name ]{.c1}

[id: ippool id ]{.c1}

[-ip: ippool ip to use ]{.c1}

[update vsphere ippool -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: ippool id ]{.c1}

[-name: ippool name ]{.c1}

[-startip: start ip ]{.c1}

[-stopip: stop ip ]{.c1}

[-gw: gateway ]{.c1}

[-dns1: dns1 ]{.c1}

[-dns2: dns2 ]{.c1}

[-prefix: prefix]{.c1}

[-dnssuffix: dns zone ]{.c1}

[platform vsphere ipset-add add vsphere ipset -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[name: ipset name ]{.c1}

[desc: ipset description ]{.c1}

[cidr: list of ip. Ex. 10.112.201.8-10.112.201.14 or cidr ]{.c1}

[platform vsphere ipset-del delete vsphere ipset -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: ipset id ]{.c1}

[platform vsphere ipset-get get ipsets -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: ipset id ]{.c1}

[-range: ipset range ]{.c1}

[platform vsphere ipset update ]{.c1}

[update vsphere ipset -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: ipset id ]{.c1}

[-name: ipset name ]{.c1}

[platform vsphere lg-del delete logical switch -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: logical switch id ]{.c1}

[platform vsphere lg-get get logical switch -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: logical switch id ]{.c1}

[-dvpg: dvpg id ]{.c1}

[platform vsphere nsx controller-get ]{.c1}

[platform vsphere nsx manager-event-get ]{.c1}

[platform vsphere nsx manager-info ]{.c1}

[platform vsphere nsx manager-reboot ]{.c1}

[get vsphere nsx manager controllers -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[get vsphere nsx manager events -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[get vsphere nsx manager info -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[reboot vsphere nsx manager -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[platform vsphere ping ping vsphere -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[platform vsphere respool del ]{.c1}

[platform vsphere respool get ]{.c1}

[platform vsphere server add ]{.c1}

[platform vsphere server console ]{.c1}

[delete resource pool -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: resource pool id ]{.c1}

[get resource pools -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[-id: resource pool id ]{.c1}

[add vsphere server \[todo:\] -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[name: server name ]{.c1}

[startip: start ip ]{.c1}

[stopip: stop ip ]{.c1}

[gw: gateway ]{.c1}

[dns1: dns1 ]{.c1}

[dns2: dns2 ]{.c1}

[-prefix: prefix ]{.c1}

[-dnssuffix: dns zone ]{.c1}

[get vsphere server console -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[platform vsphere server-del delete vsphere server -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[id: server id ]{.c1}

[platform vsphere server device-get ]{.c1}

[platform vsphere server disable-firewall ]{.c1}

[platform vsphere server disk-add ]{.c1}

[platform vsphere server disk-del ]{.c1}

[get vsphere server devices -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[disable vsphere server firewall -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[pwd: server admin password ]{.c1}

[add disk to vsphere server -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[server\_id: server id ]{.c1}

[size: disk size ]{.c1}

[datastore\_id: datastore id ]{.c1}

[delete disk from vsphere server -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name]{.c1}

[platform vsphere server disk-extend ]{.c1}

[platform vsphere server disk-get ]{.c1}

[server\_id: server id ]{.c1}

[disk\_object\_id: disk object id ]{.c1}

[extend disk of vsphere server -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[disk\_object\_id: disk object id ]{.c1}

[size: disk size in Gb ]{.c1}

[get disk of vsphere server -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[platform vsphere server-get get servers -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: server id ]{.c1}

[-name: server name ]{.c1}

[-names: filter by name like ]{.c1}

[-template: true list only template ]{.c1}

[-ipaddress: server ipaddress ]{.c1}

[-dnsname: server dnsname ]{.c1}

[-cluster: cluster id ]{.c1}

[platform vsphere server guest-info ]{.c1}

[get vsphere server guest info -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[platform vsphere server guest-run-cmd ]{.c1}

[run vsphere server command using guest tool ]{.c1}

[-O, \--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name id: server id ]{.c1}

[cmd: command ]{.c1}

[user: user ]{.c1}

[pwd: password ]{.c1}

[-params: command params. Use + as space ]{.c1}

[platform vsphere server network-destroy-config ]{.c1}

[platform vsphere server network-setup ]{.c1}

[platform vsphere server-sg add ]{.c1}

[platform vsphere server-sg del ]{.c1}

[platform vsphere server-sg get ]{.c1}

[platform vsphere server snapshot-add ]{.c1}

[platform vsphere server snapshot-del ]{.c1}

[platform vsphere server snapshot-get ]{.c1}

[platform vsphere server snapshot-revert ]{.c1}

[setup vsphere server network -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[user: user ]{.c1}

[pwd: password ]{.c1}

[ipaddr: ip address ]{.c1}

[setup vsphere server network -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[user: user ]{.c1}

[pwd: password ]{.c1}

[ipaddr: ip address ]{.c1}

[-prefix: ip address ]{.c1}

[-macaddr: mac address ]{.c1}

[gw: network gateway ]{.c1}

[hostname: hostname ]{.c1}

[dns: comma separated list of dns ]{.c1}

[dns\_search: dns search ]{.c1}

[add security to server -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[sgid: security group id ]{.c1}

[remove security from server -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[sgid: security group id ]{.c1}

[get vsphere server security groups -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: server id ]{.c1}

[create vsphere server snapshot -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[name: snapshot name ]{.c1}

[delete vsphere server snapshot -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[snapshot: snapshot id ]{.c1}

[get vsphere server snapshot -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[-snapshot: snapshot id ]{.c1}

[revert vsphere server to snapshot -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[snapshot: snapshot id ]{.c1}

[platform vsphere server- change vsphere server password -O,
\--orchestrator: vsphere platform reference label]{.c1}

[ssh-change-pwd -P, \--project: vsphere current project name id: server
id ]{.c1}

[user: user ]{.c1}

[pwd: password ]{.c1}

[newpwd: new password ]{.c1}

[platform vsphere server ssh-copy-id ]{.c1}

[platform vsphere server start ]{.c1}

[platform vsphere server stop ]{.c1}

[copy ssh key on server -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[user: user ]{.c1}

[pwd: password ]{.c1}

[pubkey: ssh public key to set. Specify file name where key is stored
]{.c1}

[start vsphere server -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[stop vsphere server -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[id: server id ]{.c1}

[platform vsphere sg-del delete vsphere securitygroup -O,
\--orchestrator: vsphere platform reference label -P, \--project:
vsphere current project name ]{.c1}

[id: securitygroup id ]{.c1}

[-force: if true force delete ]{.c1}

[platform vsphere sg-get get securitygroups -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: securitygroup id ]{.c1}

[platform vsphere sg ]{.c1}

[member-add ]{.c1}

[platform vsphere sg ]{.c1}

[member-del ]{.c1}

[platform vsphere transport zone-get ]{.c1}

[add vsphere securitygroup member -O, \--orchestrator: vsphere platform
reference label -P, \--project: vsphere current project name ]{.c1}

[id: securitygroup id ]{.c1}

[member: member to add ]{.c1}

[delete vsphere securitygroup member -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[id: securitygroup id ]{.c1}

[member: member to remove ]{.c1}

[get nsx transport zones -O, \--orchestrator: vsphere platform reference
label -P, \--project: vsphere current project name ]{.c1}

[-id: transport zone id ]{.c1}

[platform vsphere vapp-get get vapps -O, \--orchestrator: vsphere
platform reference label -P, \--project: vsphere current project name
]{.c1}

[-id: vapp id ]{.c1}

[platform vsphere version get vsphere version -O, \--orchestrator:
vsphere platform reference label -P, \--project: vsphere current project
name ]{.c1}

[platform zabbix   (zabbix platform) ]{.c2}

[platform zabbix action-add add action -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[name: action name ]{.c1}

[usrgrp\_id: usrgrp id ]{.c1}

[hostgroup\_id: hostgroup id ]{.c1}

[platform zabbix action-del delete action -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: action id ]{.c1}

[platform zabbix action-get list actions -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix current project name
]{.c1}

[-id: action id ]{.c1}

[-eventsource: eventsource id - 0 = trigger, 2 = auto registration
]{.c1}

[platform zabbix action update-trigger ]{.c1}

[update action trigger -O, \--orchestrator: zabbix platform reference
label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[action\_id: action id ]{.c1}

[hostgroup\_id: hostgroup id ]{.c1}

[severity: severity (number) ]{.c1}

[platform zabbix action- update action trigger -O, \--orchestrator:
zabbix platform reference label]{.c1}

[update-trigger-severity -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or 1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[action\_id: action id ]{.c1}

[severity: severity (number) ]{.c1}

[platform zabbix alert-get list alerts -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: alert id ]{.c1}

[-field: sort field ]{.c1}

[platform zabbix host-add add host -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix current project name ]{.c1}

[file: data file ]{.c1}

[platform zabbix host-del delete host -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[platform zabbix host disable ]{.c1}

[disable host -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[platform zabbix host-enable enable host -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[platform zabbix host-get list hosts -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: host id ]{.c1}

[-field: sort field ]{.c1}

[-name: host name ]{.c1}

[platform zabbix host-get groups ]{.c1}

[platform zabbix host-get interfaces ]{.c1}

[platform zabbix host-get templates ]{.c1}

[platform zabbix host-item add ]{.c1}

[list groups the host belongs to -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[list interfaces used by the host -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[list templates linked to the host -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: host id ]{.c1}

[add host item -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix current project name ]{.c1}

[id: host id ]{.c1}

[name: key name ]{.c1}

[desc: item description/comment ]{.c1}

[agent\_type: zabbix type. Can be: 0 - Zabbix agent, 1 - SNMPv1 agent,
]{.c1}

[2 - Zabbix trapper, 3 - simple check, 4 - SNMPv2 agent, 5 - Zabbix
]{.c1}

[internal, 6 - SNMPv3 agent, 7 - Zabbix agent (active), 8 - Zabbix
]{.c1}

[aggregate, 9 - web item, 10 - external check, 11 - database monitor, 12
]{.c1}

[- IPMI agent, 13 - SSH agent, 14 - TELNET agent, 15 - calculated, 16 -
]{.c1}

[JMX agent.]{.c1}

[platform zabbix host-item get ]{.c1}

[platform zabbix host trigger-get ]{.c1}

[platform zabbix hostgroup add ]{.c1}

[platform zabbix hostgroup del ]{.c1}

[platform zabbix hostgroup get ]{.c1}

[platform zabbix hostgroup get-hosts ]{.c1}

[platform zabbix hostgroup get-templates ]{.c1}

[platform zabbix hostgroup update ]{.c1}

[platform zabbix interface del ]{.c1}

[platform zabbix interface get ]{.c1}

[platform zabbix interface get-hosts ]{.c1}

[value\_type: zabbix value\_type. Can be: 0 - numeric float, 1 -
character, ]{.c1}

[2 - log, 3 - numeric unsigned, 4 - text. ]{.c1}

[interfaceid: zabbix host interfaceid ]{.c1}

[key: item key ]{.c1}

[delay: check interval in seconds ]{.c1}

[history: number of days to keep item history data ]{.c1}

[trends: number of days to keep item trends data ]{.c1}

[list host items -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix current project name ]{.c1}

[-id: host id ]{.c1}

[-name: host name ]{.c1}

[-state: host state ]{.c1}

[list host triggers -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix current project name ]{.c1}

[id: host id ]{.c1}

[add group -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[name: group name ]{.c1}

[delete group -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[list groups -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: group id ]{.c1}

[-field: sort field ]{.c1}

[list hosts that belong to a group -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[list templates that belong to a group -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[update group -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[name: group name ]{.c1}

[delete interface -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[list interfaces -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: group id ]{.c1}

[list hosts that use the interface -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\]]{.c1}

[platform zabbix it-service get ]{.c1}

[id: group id ]{.c1}

[list it services -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: alert id ]{.c1}

[-sla: if true pirnt calculated sla ]{.c1}

[platform zabbix ping ping zabbix -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix current project name ]{.c1}

[platform zabbix problem get ]{.c1}

[list problems -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix current project name ]{.c1}

[-id: action id ]{.c1}

[platform zabbix proxy-add add proxy -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix current project name
]{.c1}

[name: proxy hostname ]{.c1}

[platform zabbix proxy-del delete proxy -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: proxy id ]{.c1}

[platform zabbix proxy-get list proxys -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: proxy id ]{.c1}

[-field: sort field ]{.c1}

[platform zabbix template add ]{.c1}

[platform zabbix template del ]{.c1}

[platform zabbix template get ]{.c1}

[platform zabbix template get-groups ]{.c1}

[platform zabbix template get-hosts ]{.c1}

[add template -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix current project name ]{.c1}

[file: data file ]{.c1}

[delete template -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: template id ]{.c1}

[list templates -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: template id ]{.c1}

[-field: sort field ]{.c1}

[list groups the template belongs to -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[list hosts linked to the template -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: group id ]{.c1}

[platform zabbix trigger-add add trigger -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix current project name
]{.c1}

[desc: trigger description ]{.c1}

[comment: trigger comment ]{.c1}

[expression: trigger expression ]{.c1}

[priority: priority type. Can be: 0 (Default) not classified, 1
information, ]{.c1}

[2 warning, 3 average, 4 high, 5 disaster ]{.c1}

[platform zabbix trigger-del delete trigger -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\]]{.c1}

[id: trigger id ]{.c1}

[platform zabbix trigger-get list triggers -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: trigger id ]{.c1}

[-field: sort field ]{.c1}

[-host: host id filter ]{.c1}

[platform zabbix user-add add user -O, \--orchestrator: zabbix platform
reference label -P, \--project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[username: user name ]{.c1}

[passwd: password ]{.c1}

[usrgrpid: user group id ]{.c1}

[email: user email ]{.c1}

[platform zabbix user-del delete user -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: user id ]{.c1}

[platform zabbix user-get list users -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix current project name
]{.c1}

[-id: user id ]{.c1}

[platform zabbix user-update update user -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[user\_id: user id ]{.c1}

[email: users email - separated by comma ]{.c1}

[severity: severity - 48 default (32 Disaster + 16 High) ]{.c1}

[platform zabbix usergroup add ]{.c1}

[platform zabbix usergroup del ]{.c1}

[platform zabbix usergroup get ]{.c1}

[add usergroup -O, \--orchestrator: zabbix platform reference label -P,
\--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or
]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[usergroupname: usergroup name ]{.c1}

[hostgroup\_id: hostgroup id ]{.c1}

[delete user group -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: user group id ]{.c1}

[list user groups -O, \--orchestrator: zabbix platform reference label
-P, \--project: zabbix host group name or id. e.g. Csi.Datacenter.Test
or ]{.c1}

[1234.. ]{.c1}

[-size: list page size \[default=20\] ]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: user group id ]{.c1}

[-field: sort field ]{.c1}

[platform zabbix version get zabbix version -O, \--orchestrator: zabbix
platform reference label -P, \--project: zabbix current project name
]{.c1}

[res   (resource management) ]{.c301}

[res containers   (resource container management)]{.c2}

[res containers add add resource container -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[file: container config as file ]{.c1}

[res containers delete delete resource container -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: container uuid ]{.c1}

[res containers discover discover container id: entity uuid resclass:
entity resclass ]{.c1}

[res containers discover types ]{.c1}

[discover container resources id: entity uuid ]{.c1}

[res containers discovers discover container id: entity uuid ]{.c1}

[res containers get list resource containers -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: container uuid ]{.c1}

[-name: container name ]{.c1}

[-container\_type: container type ]{.c1}

[-objid: container authorization id ]{.c1}

[-state: container state ]{.c1}

[-attributes: container attributes ]{.c1}

[-tags: entity tags ]{.c1}

[-container\_type\_name: container type name ]{.c1}

[res containers ping ping resource container id: entity uuid ]{.c1}

[res containers pings ping all resource containers ]{.c1}

[res containers synchronize synchronize container resources id:
container id ]{.c1}

[resclass: entity resclass ]{.c1}

[-new: add new physical entities ]{.c1}

[-died: delete not alive physical entities ]{.c1}

[-changed: update physical entities ]{.c1}

[-ext\_id: physical entity id ]{.c1}

[res containers synchronizes synchronize container resources id: entity
uuid ]{.c1}

[res containers types list resource container types ]{.c1}

[res containers update update resource container -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: container uuid ]{.c1}

[file: container config as file ]{.c1}

[res entities   (entities management) ]{.c2}

[res entities add add resource entity name: resource entity name -desc:
resource entity description ]{.c1}

[container: resource container uuid ]{.c1}

[resclass: resource entity class ]{.c1}

[-ext\_id: resource entity physical id ]{.c1}

[-parent: resource entity parent uuid ]{.c1}

[-attribute: resource entity attributes ]{.c1}

[-tags: resource entity tags ]{.c1}

[res entities cache-del delete resource entity cache id: resource entity
id ]{.c1}

[res entities cache-get get resource entity cache id: resource entity id
]{.c1}

[res entities check check resource entity id: resource entity id ]{.c1}

[res entities config-get get resource entity config id: resource entity
id ]{.c1}

[res entities config-set update resource entity config id: resource
entity id ]{.c1}

[key: config key like config.key ]{.c1}

[-value: config value ]{.c1}

[res entities delete delete resource entities ids: comma separated
resource entity ids -force: if true force the delete ]{.c1}

[-deep: if false delete only resource record and permissions ]{.c1}

[res entities disable-quotas disable resource quotas and metrics
discover ]{.c1}

[res entities enable-quotas enable resource quotas and metrics discover
]{.c1}

[id: resource entity id id: resource entity id ]{.c1}

[res entities errors get the last resource error from a job entity:
resource entity is or name]{.c1}

[res entities get list resource entities -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: entity id ]{.c1}

[-name: entity name ]{.c1}

[-desc: entity description ]{.c1}

[-container: container uuid or name ]{.c1}

[-type: entity type ]{.c1}

[-objid: entity authorization id ]{.c1}

[-ext\_id: entity physical id ]{.c1}

[-parent: entity parent ]{.c1}

[-state: entity state ]{.c1}

[-attributes: entity attributes ]{.c1}

[-tags: entity tags ]{.c1}

[res entities linked get linked resource entities id: resource entity id
]{.c1}

[res entities metrics get resource entity metrics id: resource entity id
]{.c1}

[res entities patch patch resource entities ids: comma separated
resource entity ids ]{.c1}

[res entities state reset resource state id: resource entity id ]{.c1}

[-state: resource state ]{.c1}

[res entities tag-add add tag to resource id: resource entity id ]{.c1}

[tag: tag name ]{.c1}

[res entities tag-del remove tag from resource id: resource entity id
]{.c1}

[tag: tag name ]{.c1}

[res entities tag-get get tags of resource -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource id ]{.c1}

[res entities tree get resource entity tree entity: resource entity is
or name -parent: if True show tree by parent - child ]{.c1}

[-link: if True show tree by link relation ]{.c1}

[res entities types list resource entity types -type: entity type ]{.c1}

[-subsystem: entity type subsystem ]{.c1}

[res entities update update resource entity id: resource entity id
]{.c1}

[-name: resource entity name ]{.c1}

[-desc: resource entity description ]{.c1}

[-active: resource entity active ]{.c1}

[-force: if True force resource metadata update and bypass type ]{.c1}

[specific update ]{.c1}

[-ext\_id: resource physical id ]{.c1}

[-attribute: resource entity attributes ]{.c1}

[res links   (links management) ]{.c2}

[res links add add resource link name: resource link name ]{.c1}

[type: resource link type ]{.c1}

[start\_resource: start resource uuid ]{.c1}

[end\_resource: end resource uuid ]{.c1}

[-attributes: resource link attributes ]{.c1}

[res links delete delete resource links ids: comma separated resource
link uuids -force: if true force the delete ]{.c1}

[res links get list resource links -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: link uuid ]{.c1}

[-name: link name ]{.c1}

[-resource: start or end resource uuid ]{.c1}

[-type: link type ]{.c1}

[-objid: link authorization id ]{.c1}

[-tags: link tags ]{.c1}

[res links patch patch resource links ids: comma separated resource link
uuids ]{.c1}

[res links update update resource link id: resource link uuid ]{.c1}

[-name: resource link name ]{.c1}

[-type: resource link type ]{.c1}

[-start\_resource: start resource uuid ]{.c1}

[-end\_resource: end resource uuid ]{.c1}

[-attributes: resource link attributes]{.c1}

[res tags   (tags management) ]{.c2}

[res tags add add resource tag value: resource tag value ]{.c1}

[res tags delete delete resource tags ids: comma separated resource tag
uuids -force: if true force the delete ]{.c1}

[res tags get list resource tags -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: tag uuid ]{.c1}

[-name: tag name ]{.c1}

[-resource: resource ]{.c1}

[-container: container uuid or name ]{.c1}

[-type: tag type ]{.c1}

[-objid: tag authorization id ]{.c1}

[-ext\_id: tag physical id ]{.c1}

[-parent: tag parent ]{.c1}

[-state: tag state ]{.c1}

[-attributes: tag attributes ]{.c1}

[-tags: tag tags ]{.c1}

[res tags patch patch resource tags ids: comma separated resource tag
uuids ]{.c1}

[res tags update update resource tag id: resource tag uuid -value:
resource tag value ]{.c1}

[res-awx   (awx orchestrator) ]{.c301}

[res-awx job-template-get get job templates -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: job template id ]{.c1}

[res-awx project-get get projects -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: project id ]{.c1}

[res-dns   (dns orchestrator) ]{.c301}

[res-dns record-cname-add create new record CNAME (alias -\>
hostname.zone) ]{.c1}

[-size: list page size \[default=20\] -page: list page \[default=0\]
]{.c1}

[-field: list sort field \[default=id\] -order: list sort order
\[default=DESC\] name: alias to set ]{.c1}

[hostname: host name ]{.c1}

[zone: zone name ]{.c1}

[-ttl: time to live ]{.c1}

[res-dns record-cname delete ]{.c1}

[delete an existing record CNAME -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: record id ]{.c1}

[res-dns record-cname-get get dns record cnames -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: project id ]{.c1}

[-name: dns name ]{.c1}

[-host\_name: host name ]{.c1}

[-parent: zone name ]{.c1}

[-show\_expired: if True show record DELETED ]{.c1}

[res-dns recorda-add create new record A (ip address -\> hostname.zone)
]{.c1}

[res-dns recorda-delete delete an existing record A (ip address -\>
hostname.zone) ]{.c1}

[-size: list page size \[default=20\] -page: list page \[default=0\]
]{.c1}

[-field: list sort field \[default=id\] -order: list sort order
\[default=DESC\] ipaddress: ip address ]{.c1}

[hostname: host name ]{.c1}

[zone: zone name ]{.c1}

[-ttl: time to livee ]{.c1}

[-size: list page size \[default=20\] -page: list page
\[default=0\]]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: record id ]{.c1}

[res-dns recorda-get get dns recordas -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: project id ]{.c1}

[-name: dns name ]{.c1}

[-ip\_addr: ip address ]{.c1}

[-parent: zone name ]{.c1}

[-show\_expired: if True show record DELETED ]{.c1}

[res-dns zone-get get zones -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: project id ]{.c1}

[res-dns zone-query fetch a zone record -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: zone id ]{.c1}

[record: record name ]{.c1}

[res-dns zone-records-import import record in a zone reading from a file
]{.c1}

[res-elk   (elk orchestrator) ]{.c301}

[-size: list page size \[default=20\] -page: list page \[default=0\]
]{.c1}

[-field: list sort field \[default=id\] -order: list sort order
\[default=DESC\] id: zone id ]{.c1}

[filename: file name ]{.c1}

[res-elk role-add add roles -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[name: role name ]{.c1}

[indice: indice ]{.c1}

[space\_id: space id ]{.c1}

[res-elk role-delete delete roles -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource role id ]{.c1}

[res-elk role-get get roles -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: role id ]{.c1}

[res-elk role-mapping-add add role\_mappings -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[name: role\_mapping name ]{.c1}

[role\_name: role name ]{.c1}

[users\_email: users email ]{.c1}

[realm\_name: realm name ]{.c1}

[res-elk role-mapping-delete delete role\_mappings -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource role\_mapping id ]{.c1}

[res-elk role-mapping-get get role\_mappings -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: role\_mapping id ]{.c1}

[res-elk space-add add spaces -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[id: space id]{.c1}

[name: space name ]{.c1}

[-description: space description ]{.c1}

[-color: space color ]{.c1}

[-initials: space initials ]{.c1}

[res-elk space-delete delete spaces -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource space id ]{.c1}

[res-elk space-get get spaces -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: space id ]{.c1}

[res-grafana   (grafana orchestrator) ]{.c301}

[res-grafana alert notification-add ]{.c1}

[res-grafana alert notification-delete ]{.c1}

[res-grafana alert notification-get ]{.c1}

[add alert\_notifications -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[name: alert\_notification name ]{.c1}

[email: alert\_notification email ]{.c1}

[-desc: alert\_notification desc ]{.c1}

[delete alert\_notifications -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource alert\_notification id ]{.c1}

[get alert\_notifications -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: alert\_notification id ]{.c1}

[res-grafana folder-add add folders -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[name: folder name ]{.c1}

[-desc: folder desc ]{.c1}

[res-grafana folder-delete delete folders -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource folder id ]{.c1}

[res-grafana folder-get get folders -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: folder id ]{.c1}

[res-grafana team-add add teams -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container ]{.c1}

[name: team name ]{.c1}

[-desc: team desc ]{.c1}

[res-grafana team-delete delete teams -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: resource team id ]{.c1}

[res-grafana team-get get teams -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: team id ]{.c1}

[res-openstack   (openstack orchestrator)]{.c301}

[res-openstack domain-get get domains -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: domain id ]{.c1}

[res-openstack flavor-get get flavors -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: flavor id ]{.c1}

[res-openstack image-get get images -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: image id ]{.c1}

[res-openstack network-get get networks -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: network id ]{.c1}

[res-openstack port-get get ports -size: list page size \[default=20\]
-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: port id ]{.c1}

[res-openstack project default-quota-get ]{.c1}

[get project default quotas -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: project id ]{.c1}

[res-openstack project-get get projects -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: project id ]{.c1}

[res-openstack project member-get ]{.c1}

[res-openstack project member-set ]{.c1}

[res-openstack project quota-get ]{.c1}

[res-openstack project quota-set ]{.c1}

[get project members -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: project id ]{.c1}

[set project member TODO -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: project id ]{.c1}

[type: quota type ]{.c1}

[quota: quota name ]{.c1}

[value: quota value ]{.c1}

[get project quotas -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: project id ]{.c1}

[set project quotas -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: project id ]{.c1}

[type: quota type ]{.c1}

[quota: quota name ]{.c1}

[value: quota value ]{.c1}

[res-openstack router-get get routers -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: router id ]{.c1}

[res-openstack router-port del ]{.c1}

[res-openstack security group-del-rule ]{.c1}

[delete router port -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[id: router id ]{.c1}

[subnet: subnet id ]{.c1}

[delete security group rule -size: list page size \[default=20\] -page:
list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\]]{.c1}

[res-openstack security group-get ]{.c1}

[res-openstack server actions ]{.c1}

[res-openstack server console ]{.c1}

[id: security group id ]{.c1}

[rule: security group rule id ]{.c1}

[get security groups -size: list page size \[default=20\] -page: list
page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: security group id ]{.c1}

[get server actions id: server id ]{.c1}

[get server console id: server id ]{.c1}

[res-openstack server-del delete server id: server id ]{.c1}

[res-openstack server-get get servers -size: list page size
\[default=20\] -page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[-id: server id ]{.c1}

[-name: instance name ]{.c1}

[-desc: instance description ]{.c1}

[-parent: instance parent ]{.c1}

[-state: instance state ]{.c1}

[-tags: instance tags ]{.c1}

[-container: container uuid or name ]{.c1}

[res-openstack server metadata ]{.c1}

[get server metadata id: server id ]{.c1}

[res-openstack server-patch patch server id: server id ]{.c1}

[res-openstack server-resize get server security groups id: server id
flavor: flavor id ]{.c1}

[res-openstack server runtime ]{.c1}

[get server console id: server id ]{.c1}

[res-openstack server-sg-add add openstack server security group id:
server id sg: security group id ]{.c1}

[res-openstack server-sg-del delete openstack server security group id:
server id sg: security group id ]{.c1}

[res-openstack server snapshot-add ]{.c1}

[res-openstack server snapshot-del ]{.c1}

[res-openstack server snapshot-get ]{.c1}

[res-openstack server snapshot-revert ]{.c1}

[add openstack server snapshot id: server id name: snapshot name ]{.c1}

[delete openstack server snapshot id: server id snapshot: snapshot id
]{.c1}

[get openstack server snapshots id: server id ]{.c1}

[revert openstack server to snapshot id: server id snapshot: snapshot id
]{.c1}

[res-openstack server-start get server security groups id: server id
res-openstack server-stats get server stats id: server id res-openstack
server-stop stop server id: server id ]{.c1}

[res-openstack server volume-add ]{.c1}

[res-openstack server volume-del ]{.c1}

[add volume to server id: server id volume: volume id ]{.c1}

[get server security groups id: server id volume: volume id ]{.c1}

[res-openstack share-add add share -size: list page size \[default=20\]
]{.c1}

[-page: list page \[default=0\] ]{.c1}

[-field: list sort field \[default=id\] ]{.c1}

[-order: list sort order \[default=DESC\] ]{.c1}

[container: container id ]{.c1}

[name: share name ]{.c1}

[-desc: share description ]{.c1}

[project: share project id ]{.c1}

[-tags: comma separated list of tags ]{.c1}

[share\_proto: share protocol. A valid value is NFS, CIFS, GlusterFS,
]{.c1}

[HDFS, or CephFS ]{.c1}

[size: the share size, in GBs ]{.c1}

[share\_type: The share type id. ]{.c1}

[-snapshot\_id: The id of the share\'s base snapshot. ]{.c1}

[-share\_group\_id: The id of the share group. ]{.c1}

[-network: id of the network to use ]{.c1}

[-subnet: id of the subnet to use ]{.c1}

[-metadata: One or more metadata key and value pairs as a dictionary
]{.c1}

[of strings. ]{.c1}

[-availability\_zone: The availability zone. ]{.c1}

[res-openstack share-del delete share -size: list page size
\[default=20\] ]{.c1}

[-page: list page \[default=0\]]{.c1}
