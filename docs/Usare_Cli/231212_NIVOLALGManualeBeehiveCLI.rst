
**Manuale Beehive Command Line Interface**
******************************************

Beehive CLI

ask ask command -eq: search equal command -a: command to search

bash-completion get bash completion script

bash-completion-envs get bash completion envs

decrypt decrypt quoted data with symmetric encryption

data: data to decrypt

key: secret key to use for encryption/decryption

encrypt encrypt data with symmetric encryption data: data to encrypt

key: secret key to use for encryption/decryption

envs list available environments -maxcolwidth: max column width.
default=50 -multichunks: split the output in chunks

-current: list only current environment

-orchestrator_type_name: Filter by orchestrator type name. e.g. zabbix

gen-key generate fernet key for symmetric

encryption

gen-password generate password -length: password length

-strong: password strong

tree tree command

auth   (authorization management)

auth groups   (groups management)

auth groups add add group name: group name

-desc: group description

-expirydate: group expire date. Syntax yyyy-mm-dd

auth groups add-attrib add attribute to group id: group uuid

attrib: attribute name

value: attribute value

desc: attribute description

auth groups add-perms add permissions to group id: group uuid

perms: comma separated list of permission id

auth groups add-role add role to group id: group uuid

role: role uuid

-expirydate: group expire date. Syntax yyyy-mm-dd

auth groups add-user add user to group id: group uuid

user: user uuid

auth groups del-attrib delete attribute from group id: group uuid

attrib: attribute name

auth groups del-perms delete permissions from group id: group uuid

perms: comma separated list of permission id

auth groups del-role delete role from group id: group uuid

role: role uuid

auth groups del-user delete user from group id: group uuid

user: user uuid

auth groups delete delete group id: group uuid

auth groups get get groups -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: account uuid

-role: role id or name

-user: user id or name

-name: name filter

-desc: group desc

-email: email address

-expiry-date : expiry date. Syntax YYYY-MM-DD

-perms: rcomma separated list of permissions

auth groups get-perms get permissions of group -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: group uuid

auth groups update update group id: group uuid -name: group name

-desc: group description

-active: group active

auth ldap   (ldap management)

auth ldap get get user key: user key like user email -filter: search
filter

-ldap: ldap reference label

auth ldap login login user email: user email pwd: user password

-ldap: ldap reference label

auth ldap search search users value: value to search -filter: search
filter

-fields: query fields

-ldap: ldap reference label

auth oauth2-authorization-codes   (oauth2 authorization code)

auth oauth2-authorization codes delete

auth oauth2-authorization codes get

delete oauth2 authorization code id: comma separated authorization code
ids

get oauth2 authorization codes -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: authorization code id

-valid: valid

-client: client

-user:

auth oauth2-clients   (oauth2 client)

auth oauth2-clients add add oauth2 client name: client name

grant_type: valid grant_type: authorization_code, implicit, password,

client_credentials, urn:ietf:params:oauth:grant-type:jwt-bearer

-redirect_uri: redirect_uri

-scopes: comma separated list of scopes

-expirydate: client expire date. Syntax yyyy-mm-dd

auth oauth2-clients delete delete oauth2 client id: client uuid

auth oauth2-clients get get oauth2 clients -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: client uuid

-role: role uuid

-group: group uuid

-name: name filter

-desc: client desc

-email: email address

-expiry-date : expiry date. Syntax YYYY-MM-DD

-perms: comma separated list of permission id

auth oauth2-scopes   (oauth2 scope)

auth oauth2-scopes add add oauth2 scope name: scope name

auth oauth2-scopes delete delete oauth2 scope id: scope uuid

auth oauth2-scopes get get oauth2 scopes -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: scope uuid

auth oauth2-tokens   (oauth2 token)

auth oauth2-tokens create create oauth2 access token using
resource_owner or client_credentials

grant. For resource_owner grant specify

user and pwd. For client_credentials

specify client secret.

auth oauth2-user-sessions   (oauth2 user session)

client: client id

-user: login user -pwd: user password -secret: client secret

auth oauth2-user-sessions delete

auth oauth2-user-sessions get

delete oauth2 session id: comma separated session ids

get oauth2 sessions -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: session id

auth perms   (permission management)

auth perms add-object add object desc: user description objid:
autorization id

subsystem: subsystem

type: type

auth perms add-type add object type -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: subsystem

type: type

auth perms del-object delete object ids: comma separated list of object
id auth perms del-type delete object type id: object type uuid

auth perms get get permission -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: permission id

auth perms get-actions get object actions

auth perms get-method get method -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

rule: method url/rule

-subsystem: subsystem

auth perms get-objects get objects -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: object id

-objid: autorization id

-subsystem: subsystem

-type: type

auth perms get-types get object types -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: account uuid

-subsystem: subsystem

-type: type

auth providers   (authentication provider management)

auth providers get get authentication providers

auth roles   (roles management)

auth roles add add role name: role name -desc: role description

auth roles add-perms add permissions to role id: role uuid

perms: comma separated list of permission id

auth roles del-perms delete permissions from role id: role uuid

perms: comma separated list of permission id

auth roles delete delete role id: role uuid

auth roles get get roles -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: account uuid

-user: role uuid

-group: group uuid

-names: name filter

-alias: role alias

-perms: comma separated list of permission id

auth roles get-perms get permissions of role -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: role uuid

auth roles reset-role reset permissions to full user permission

auth roles update update role id: role uuid

-name: role name

-desc: role description

auth roles use-role Use role roleid: role uuid

auth tokens   (tokens management)

auth tokens add create keyauth or oauth2 jwt token -type: can be
keyauth, oauth2. oauth2 create a token using a jwt client user: login
user

pwd: login password

-client: ouath2 client uuid

-sub: sub field for oauth2 jwt login

auth tokens delete delete token id: token uuid or all for all

auth tokens get get tokens -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: token uuid

auth tokens get-my-token return your own authentication token

auth users   (users management)

auth users add add user name: user name

-desc: user description

-storetype: can be DBUSER, LDAPUSER

-password: user password. Set only for DBUSER

-expirydate: user expire date. Syntax yyyy-mm-dd

-email: email address

auth users add-attrib add attribute to user id: user uuid

attrib: attribute name

value: attribute value

desc: attribute description

auth users add-group add group to user id: user uuid

group: group uuid

auth users add-perms add permissions to user id: user uuid

perms: comma separated list of permission id

auth users add-role add role to user id: user uuid

role: role uuid

-expirydate: user expire date. Syntax yyyy-mm-dd

auth users add-system add system user name: user name

password: user password. Set only for DBUSER

auth users del-attrib delete attribute from user id: user uuid

attrib: attribute name

auth users del-group delete group from user id: user uuid

group: group uuid

auth users del-perms delete permissions from user id: user uuid

perms: comma separated list of permission id

auth users del-role delete role from user id: user uuid

role: role uuid

auth users delete delete user id: user uuid

auth users get get users -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: user uuid

-role: role uuid

-group: group uuid

-name: name filter

-desc: user desc

-email: email address

-expiry-date: expiry date. Syntax YYYY-MM-DD

-perms: comma separated list of permission id

auth users get-perms get permissions of user -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: user uuid

auth users get-secret get user secret id: user uuid

auth users update update user id: user uuid

-name: user name

-desc: user description

-active: user active

-provider: authentication provider

-password: user password. Set only for DBUSER

-expirydate: user expire date. Syntax yyyy-mm-dd

-email: email address

bu   (business service and authority management)

bu accounts   (account management)

bu accounts add add account name: account name -desc: account
description

division: division uuid

-contact: account contact

-email: account email

-email-support: account email support

-email-support-link: account email support link

-note: account note

-acronym: account acronym

-managed: if true set account as managed

bu accounts definition-add add account definitions -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: account id

definitions: comma separated list of definition ids

bu accounts definition-get get account definitions -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: account id

-plugintype: filter by definition plugin

-category: filet by category

-container: get only containers definitions

bu accounts delete delete account id: account id

-delete_services: if true delete all child services

bu accounts get get accounts -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: account id

-objid: authorization id

-name: account name

-division-id: division uuid

-contact: account contact

-email: account email

-email-support: account email support

bu accounts manage Aminister account -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: the account id to manage

bu accounts operate Operate on account -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: the account id to manage

bu accounts patch refresh account id: account id

bu accounts service-active get

get account active services info id: account id

bu accounts service-del delete account services id: account id

bu accounts update update account id: account id

-desc: account description

-price_list: account price list id

-contact: account contact

-email: account email

-email-support: account email support

-email-support-link: account email support link

-acronym: account acronym

-note: account note

bu accounts user-role-get get account user roles id: account id

bu accounts view View account -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: the account id to manage

bu accounts-auth   (account authorization)

bu accounts-auth group-add add account role to a group id: account id

role: account role

group: authorization group

bu accounts-auth group-del remove account role from a group id: account
id

role: account role

group: authorization group

bu accounts-auth group-get get account groups id: account id

bu accounts-auth role-get get account roles id: account id

bu accounts-auth user-add add account role to a user id: account id

role: account role

user: authorization user

bu accounts-auth user-del remove account role from a user id: account id

role: account role

user: authorization user

bu accounts-auth user-get get account users id: account id

bu accounts-capabilities   (accounts capabilities)

bu accounts-capabilities add

add or update account capabilities -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: account id

capabilities: comma separated list of capability name

bu accounts-capabilities get get account capabilities id: account id
-capability: capability name

bu accounts-tags   (manage tags for account)

bu accounts-tags get get accounts -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: account id

bu appeng   (appengine service management)

bu appeng info get appengine service info account: account id bu appeng
quotas get appengine service quotas account: account id

bu appeng app-instances   (appengine instances service management)

bu appeng app-instances add

bu appeng app-instances delete

bu appeng app-instances get

bu appeng app-instances list

bu appeng app-instances types

create a share name: appengine name

account: parent account id

farm-name: name of the farm

type: appengine type

subnet: appengine subnet id

sg: security group id

-key-name: ssh key name

-sharesize: share size in GB

-public: if True appengine has public ip address

-public-subnet: public subnet

delete an appengine appengine: appengine id

get appengine appengine: appengine id

list app engine -accounts: list of account id comma separated -ida: list
of appengin id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

get appengine types

bu capabilities   (capabilities management)

bu capabilities add add capability config: capability config bu
capabilities delete delete capability id: capability uuid

bu capabilities get get capabilities -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: account uuid

-objid: authorization id

bu cpaas   (compute service management)

bu cpaas availability-zones get compute service availibility zones
account: account id bu cpaas info get compute service info account:
account id bu cpaas quotas get compute service quotas account: account
id

bu cpaas compute-tags   (tags service management)

bu cpaas compute-tags add add tag to service instance account: account
id service: service instance id

tag: tag key

bu cpaas compute-tags delete

delete tag from service instance service: service instance id tag: tag
key

bu cpaas compute-tags list list resource by tags -account: account id

-services: comma separated list of service instance id

-tags: comma separated list of tag key

-types: comma separated list of service instance types

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas customizations   (customization service management)

bu cpaas customizations add

create a customization name: customization name

account: parent account id

type: customization type

instances: comma separated list of compute instance id

args: customization params. Use syntax arg1:val1,arg2:val2

bu cpaas customizations delete

delete a customization customization: customization id

bu cpaas customizations get get customization customization:
customization id

bu cpaas customizations list list customizations -accounts: list of
account id comma separated -customizations: list of customization id
comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas customizations types

bu cpaas customizations update

get customizations types account: parent account id -id: customization
type id

-page: list page [default=0]

-size: list page size [default=20]

update a customization customization: customization id

bu cpaas images   (image service management)

bu cpaas images add create an image name: image name account: parent
account id

desc: image description

type: image type

bu cpaas images delete delete an image image: image id

bu cpaas images get get image image: image id

bu cpaas images list list images -accounts: list of account id comma
separated -images: list of image id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas images types get image templates account: account id -id:
template id

bu cpaas keypairs   (key pair management)

bu cpaas keypairs add add new RSA key pair account: account id name: key
pair name

-type: key type

bu cpaas keypairs delete delete a key pair name: keypair name bu cpaas
keypairs get get key pair name: keypair name

bu cpaas keypairs import public-key

import public RSA key account: account id

name: key pair name

publickey: file containing public key base64 encoded

-type: key type

bu cpaas keypairs list get key pairs -accounts: list of account id comma
separated -name: list of keypair name comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas vms   (virtual machine service management)

bu cpaas vms add create a virtual machine name: virtual machine name

account: parent account id

type: virtual machine type

subnet: virtual machine subnet id

image: virtual machine image id

sg: virtual machine security group id

-sshkey: virtual machine ssh key name

-pwd: virtual machine admin/root password

-main-disk: optional main disk size configuration. Use to set e default

volume type.- Use : to set a non default volume type. Ex. 5:vol.oracle

Use : to set a volume to clone

-other-disk: list of additional disk sizes comma separated. Use to set e

default volume type.Use : to set a non default volume type. Ex. 5,10 or

5:vol.oracle,10

-hypervisor: virtual machine hypervisor. Can be: openstack or vsphere

[default=openstack]

-host-group: virtual machine host group. Ex. oracle

-multi-avz: if set to False create vm to work only in the selected

availability zone [default=True]. Use when subnet cidr is public

-meta: virtual machine custom metadata

-skip-main-vol-size-check: Use to skip check that main volume size is

not smaller than the main volume of the template.

bu cpaas vms backup-job add

bu cpaas vms backup-job del

bu cpaas vms backup-job get

bu cpaas vms backup-job instance-add

bu cpaas vms backup-job instance-del

bu cpaas vms backup-job list

add account virtual machine backup job name: job name

account: account id

zone: job availability zone

instance: comma separated list of instance id to add

-hypervisor: job hypervisor [openstack]

-policy: job hypervisor [bk-job-policy-7-7-retention]

-desc: job description

delete account virtual machine backup job account: account id

job: job id

get account virtual machine backup job account: account id

job: job id

add virtual machine to backup job account: account id

job: job id

instance: instance id to add

delete virtual machine from backup job account: account id

job: job id

instance: instance id to add

get account virtual machine backup jobs account: account id

-hypervisor: virtual machine hypervisor. Can be: openstack or vsphere

bu cpaas vms backup-job policies

bu cpaas vms backup-job update

get account virtual machine backup job policies

update account virtual machine backup job

account: account id

account: account id

job: job id

-name: job name

-enabled: enable or disable job -policy: job policy

bu cpaas vms backup restore-add

bu cpaas vms backup restore-get

bu cpaas vms backup restore-point-add

bu cpaas vms backup restore-point-del

bu cpaas vms backup restore-point-get

restore a virtual machine from backup name: restored virtual machine
name id: id of the virtual machine to clone

restore_point: id of restore point

get virtual machine backup restores vm: virtual machine id

restore_point: restore point id

add backup job restore point account: account id

job: job id

name: restore point name

-desc: restore point description

-full: backup type. If true make a full backup otherwise make an

incremental backup

delete backup job restore point account: account id

job: job id

restore_point: restore point id

get backup job restore points account: virtual machine id

-vm: virtual machine id

-job: job id

-restore_point: restore point id

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas vms clone clone a virtual machine name: virtual machine name
id: id of the virtual machine to clone

-account: parent account id

-type: virtual machine type

-subnet: virtual machine subnet id

-sg: virtual machine security group id

-sshkey: virtual machine ssh key name

-pwd: virtual machine admin/root password

-multi-avz: if set to False create vm to work only in the selected

availability zone [default=True]. Use when subnet cidr is public

-meta: virtual machine custom metadata

bu cpaas vms console-get get virtual machine console vm: virtual machine
id

bu cpaas vms delete delete a virtual machine vm: virtual machine id

bu cpaas vms disable monitoring

bu cpaas vms enable logging

bu cpaas vms enable monitoring

disable virtual machine monitoring vm: virtual machine id --continues:
continue use command

enable virtual machine logging vm: virtual machine id -files: files list

-pipeline: log collector pipeline port

--continues: continue use command

enable virtual machine monitoring vm: virtual machine id -templates:
templates list

--continues: continue use command

bu cpaas vms get get virtual machine vm: virtual machine id

bu cpaas vms list get virtual machine -accounts: list of account id
comma separated -ids: list of vm id comma separated

-name: vm name

-names: vm name pattern

-types: list of type comma separated

-launch_time: launch time interval. Ex. 2021-01-30T:2021-01-31T

-tags: list of tag comma separated

-states: list of instance state comma separated

-sg: list of security group id comma separated. Ex. pending, running,

error

-page: list page [default=0]

-size: list page size [default=20]

-services: print instance service enabling. Ex. backup, monitoring

bu cpaas vms list-all list all the virtual machines start: vms range
lower bound

end: vms range upper bound

bu cpaas vms load import a virtual machine container: container id where
import virtual machine name: virtual machine name

vm: physical id of the virtual machine to import

image: provider image id

pwd: virtual machine password

-sshkey: virtual machine ssh key name

account: parent account id

bu cpaas vms reboot reboot a virtual machine vm: virtual machine id

-schedule: schedule definition. Pass as json file using crontab or

timedelta syntax. Ex. {"type": "timedelta", "minutes": 1}

bu cpaas vms refresh-state refresh virtual machine state id: virtual
machine id, uuid or name

bu cpaas vms snapshot-add add virtual machine snapshot vm: virtual
machine id

snapshot: snapshot name

bu cpaas vms snapshot-del add virtual machine snapshot vm: virtual
machine id

snapshot: snapshot id

bu cpaas vms snapshot-get list virtual machine snapshots vm: virtual
machine id

bu cpaas vms snapshot revert

revert virtual machine snapshot vm: virtual machine id snapshot:
snapshot id

bu cpaas vms start start a virtual machine vm: virtual machine id

-schedule: schedule definition. Pass as json file using crontab or

timedelta syntax. Ex. {"type": "timedelta", "minutes": 1}

bu cpaas vms stop stop a virtual machine vm: virtual machine id

-schedule: schedule definition. Pass as json file using crontab or

timedelta syntax. Ex. {"type": "timedelta", "minutes": 1}

bu cpaas vms types get virtual machine types account: parent account id

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas vms update update a virtual machine vm: virtual machine id

-type: virtual machine type

-sg_add: virtual machine security group id to add

-sg_del: virtual machine security group id to remove

bu cpaas vms user-add add virtual machine user vm: virtual machine id

name: user name

pwd: user password

key: ssh key id

bu cpaas vms user-del delete virtual machine user vm: virtual machine id

name: user name

bu cpaas vms user- set virtual machine user password vm: virtual machine
id

password-set name: user name

pwd: user password

bu cpaas volumes   (volume service management)

bu cpaas volumes add create a volume name: volume name

account: parent account id

availability_zone: volume availability_zone

type: volume type

size: volume sise

-iops: volume iops

-snapshot: volume snapshot

-hypervisor: volume hypervisor. Can be: openstack or vsphere

[default=openstack]

bu cpaas volumes attach attach a volume to an instance volume: volume id

instance: instance id

bu cpaas volumes delete delete a volume volume: volume id

bu cpaas volumes detach detach a volume to an instance volume: volume id

instance: instance id

bu cpaas volumes get get volume volume: volume id

bu cpaas volumes list list volumes -accounts: list of account id comma
separated -volumes: list of volume id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu cpaas volumes load load volumes from resources account: account id

volume_name: name

volume_resource_id: resource volume id

bu cpaas volumes types get volumes types account: parent account id

-page: list page [default=0]

-size: list page size [default=20]

bu dbaas   (database service management)

bu dbaas info get database service info account: account id

bu dbaas quotas get database service quotas account: account id

bu dbaas db-instances   (database instance service management)

bu dbaas db-instances add mysql

bu dbaas db-instances add oracle

bu dbaas db-instances add postgresql

create mysql db instance name: db instance name

account: parent account id

type: db instance type

subnet: db instance subnet id

sg: db instance security group id

version: database engine version

-pwd: db root password

-storage: data storage capacity in GB

-keyname: ssh key name

create oracle db instance name: db instance name

account: parent account id

type: db instance type

subnet: db instance subnet id

sg: db instance security group id

version: database engine version

-pwd: db root password

-keyname: ssh key name

-dbname: db name [default: ORCL0]

-lsnport: listener port [default: 1521]

-archmode: archivelog mode Y/N [default: Y]

-partopt: partitioning option Y/N [default: Y]

-charset: character set [default: WE8ISO8859P1]

-natcharset: national charset [default: AL16UTF16]

-dbfdisksize: datafiles disk size in GB [default: 30]

-recodisksize: recovery disk size in GB [default: 20]

create postgresql db instance name: db instance name

account: parent account id

type: db instance type

subnet: db instance subnet id

sg: db instance security group id

version: database engine version

-storage: amount of storage [GB] to allocate for the DB instance

-pwd: db root password

bu dbaas db-instances add sqlserver

bu dbaas db-instances database-add

bu dbaas db-instances database-del

bu dbaas db-instances database-get

bu dbaas db-instances delete

bu dbaas db-instances disable-monitoring

bu dbaas db-instances enable-logging

bu dbaas db-instances enable-monitoring

bu dbaas db-instances engines

-keyname: ssh key name

-postgis: spatial database extension

create sqlserver db instance name: db instance name account: parent
account id

type: db instance type

subnet: db instance subnet id

sg: db instance security group id

version: database engine version

-pwd: db root password

-storage: data storage capacity in GB

-keyname: ssh key name

create a db instance database/schema instance: db instance id name:
database name

charset: database charset

delete a db instance database/schema instance: db instance id name:
database name

get db instance databases/schemas instance: db instance id delete a db
instance database: db instance id disable db instance monitoring
instance: db instance id

enable db instance logging instance: virtual machine id -files: files
list

-pipeline: log collector pipeline port

enable db instance monitoring instance: db instance id -templates:
templates list

get database instance engines account: parent account id

bu dbaas db-instances get get database instance id: database id

bu dbaas db-instances list get database instances -accounts: list of
account id comma separated -ids: list of db instance id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu dbaas db-instances reboot

reboot a db instance database: db instance id

bu dbaas db-instances start start a db instance database: db instance id
bu dbaas db-instances stop stop a db instance database: db instance id

bu dbaas db-instances types get database instance types account: parent
account id -page: list page [default=0]

-size: list page size [default=20]

bu dbaas db-instances update

bu dbaas db-instances user add

bu dbaas db-instances user del

bu dbaas db-instances user get

bu dbaas db-instances user password-set

bu dbaas db-instances user priv-grant

bu dbaas db-instances user priv-revoke

update a db instance instance: db instance id

-dbi_class: db instance class to set up

-sg_add: db instance security group id to add

-sg_del: db instance security group id to remove

-resize: new amount of storage (in GiB) to allocate for the db instance

-extensions_add: db extensions to install, e.g.

name1:type1,name2:type2,... where type can be plugin or component

create a db instance user instance: db instance id

name: user name

pwd: user password

delete a db instance user instance: db instance id

name: user name

-force: force deletion

get db instance users instance: db instance id

change db instance user password instance: db instance id

name: user name

pwd: user password

grant db instance user privileges instance: db instance id

name: user name

db_name: database name. For postgres use db1 to select a database e

db1.schema1 to select schema schema1 in database db1

privileges: privileges admitted: mysql -

SELECT,INSERT,DELETE,UPDATE,ALL, postgres db - CONNECT,

postgres schema - USAGE,CREATE,ALL

revoke db instance user privileges instance: db instance id

name: user name

db_name: database name. For postgres use db1 to select a database e

db1.schema1 to select schema schema1 in database db1

privileges: privileges admitted: mysql -

SELECT,INSERT,DELETE,UPDATE,ALL, postgres db - CONNECT,

postgres schema - USAGE,CREATE,ALL

bu divs   (division management)

bu divs add add division name: division name

-desc: division description

organization: organization uuid

-contact: division contact

-email: division email

-postaladdress: division postaladdress

-price_list: division price list id

bu divs delete delete division id: division uuid

bu divs get get divisions -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: division uuid

-objid: authorization id

-name: division name

-organization-id: organization uuid

-contact: division contact

-email: division email

-postaladdress: division legalemail

bu divs patch refresh division id: division uuid

bu divs update update division name: division name

-desc: division description

organization: organization uuid

-contact: division contact

-email: division email

-postaladdress: division postaladdress

-price_list_id: division price list id

bu divs-auth   (division authorization)

bu divs-auth group-add add division role to a group id: division uuid

role: division role

group: authorization group

bu divs-auth group-del remove division role from a group id: division
uuid

role: division role

group: authorization group

bu divs-auth group-get get division groups id: division uuid

bu divs-auth role-get get division roles id: division uuid

bu divs-auth user-add add division role to a user id: division uuid

role: division role

user: authorization user

bu divs-auth user-del remove division role from a user id: division uuid

role: division role

user: authorization user

bu divs-auth user-get get division users id: division uuid

bu logaas   (logging service management)

bu logaas info get logging service info account: account id

bu logaas quotas get logging service quotas account: account id

bu logaas instances   (logging instance service management)

bu logaas instances add create a logging instance account: parent
account id

instance: instance

-definition: definition

-norescreate: don't create physical resource of the folder

bu logaas instances configs get logging module configs account: parent
account id

bu logaas instances delete delete a logging instance instance_id:
logging instance id bu logaas instances disable- disable logging module
instance_id: logging instance id

module conf: module configuration

bu logaas instances enable module

enable logging module instance_id: logging instance id conf: module
configuration

bu logaas instances get get logging instance id: logging instance id

bu logaas instances list list logging instances -accounts: list of
account id comma separated -name: list of logging instances id comma
separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu logaas spaces   (logging space service management)

bu logaas spaces add create a logging space account: parent account id
-name: space name

-definition: service definition of the space

-norescreate: don't create physical resource of the folder

bu logaas spaces delete delete a logging space logging_space_id: logging
space id bu logaas spaces get get logging space id: space id

bu logaas spaces list list logging spaces -accounts: list of account id
comma separated -name: list of logging instances id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu logaas spaces sync-users synchronize users of logging space
logging_space_id: logging space id

bu maas   (monitoring service management)

bu maas availability-zones get monitoring service availibility zones
account: account id

bu maas info get monitoring service info account: account id

bu maas quotas get monitoring service quotas account: account id

bu maas alerts   (monitoring alert service management)

bu maas alerts add create a monitoring alert account: parent account id
zone: availability zone

-name: alert name

-definition: service definition of the alert

-norescreate: don't create physical resource of the alert

bu maas alerts delete delete a monitoring alert monitoring_alert_id:
monitoring alert id bu maas alerts get get monitoring alert id: alert id

bu maas alerts list list monitoring alerts -accounts: list of account id
comma separated -name: list of monitoring instances id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu maas alerts user severities

get monitoring alert user severities

bu maas alerts user-update update user of monitoring alert id: alert id

users_email: users email that will receive alerts - comma separated

severity: list of alert severity - comma separated

bu maas folders   (monitoring folder service management)

bu maas folders add create a monitoring folder account: parent account
id

-name: folder name

-definition: service definition of the folder

-norescreate: don't create physical resource of the folder

bu maas folders dashboards get monitoring folder configs account: parent
account id

bu maas folders delete delete a monitoring folder monitoring_folder_id:
monitoring folder id

bu maas folders enable dashboard

enable monitoring dashboard folders_id: folders id conf: dashboard
configuration

bu maas folders get get monitoring folder id: folder id

bu maas folders list list monitoring folders -accounts: list of account
id comma separated -name: list of monitoring instances id comma
separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu maas folders sync-users synchronize users of monitoring folder
monitoring_folder_id: monitoring folder idbu maas monitor-instances
  (monitoring instance service management)

bu maas monitor-instances add

bu maas monitor-instances delete

bu maas monitor-instances get

bu maas monitor-instances list

create a monitoring instance account: parent account id

instance: instance

-definition: definition

-norescreate: don't create physical resource of the folder

delete a monitoring instance instance_id: monitoring instance id get
monitoring instance id: monitoring instance id

list monitoring instances -accounts: list of account id comma separated
-name: list of monitoring instances id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu netaas   (network service management)

bu netaas availability-zones get network service availibility zones
account: account id bu netaas info get network service info account:
account id bu netaas quotas get network service quotas account: account
id

bu netaas health-monitors   (health monitor service management)

bu netaas health-monitors add

bu netaas health-monitors delete

bu netaas health-monitors get

bu netaas health-monitors list

bu netaas health-monitors templates

bu netaas health-monitors update

create health monitor name: monitor name

account: parent account id

protocol: protocol used to perform targets health check: ['http',
'https',

'tcp', 'imcp', 'udp']

-desc: health monitor description

-interval: interval in seconds in which a server is to be tested

-timeout: maximum time in seconds in which a response from the

server must be received

-max_retries: maximum number of times the server is tested before it

is declared down

-method: method to send the health check request to the server: ['get',

'post', 'options']

-url: URL to GET or POST

-expected: expected string

delete health monitors ids: comma separated health monitor ids

get health monitor id: health monitor uuid or name

list health monitors -accounts: list of comma separated account ids
-ids: list of comma separated health monitor ids

-tags: list of comma separated tags

-page: list page [default=0]

-size: list page size [default=20]

get health monitor templates account: account id

-id: template id

update health monitor id: health monitor id

-interval: interval in seconds in which a server is to be tested

-timeout: maximum time in seconds in which a response from the

server must be received

-max_retries: maximum number of times the server is tested before it

is declared down

-method: method to send the health check request to the server: ['get',

'post', 'options']

-url: URL to GET or POST

-expected: expected string

bu netaas internet-gateways   (gateways service management)

bu netaas internet gateways add

create a gateway account: parent account id -template: template id

bu netaas internet gateways bastion-add

bu netaas internet gateways bastion-del

bu netaas internet gateways bastion-get

bu netaas internet gateways delete

bu netaas internet gateways get

bu netaas internet gateways list

bu netaas internet gateways patch

bu netaas internet gateways templates

bu netaas internet gateways vpc-attach

bu netaas internet gateways vpc-detach

create a gateway bastion gateway: gateway id

delete a gateway bastion gateway: gateway id

get gateway bastion gateway: gateway id

delete a gateway gateway: gateway id

get gateway gateway: gateway id

get gateways -accounts: list of account id comma separated -ids: list of
gateway id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

patch a gateway gateway: gateway id

get gateway templates account: account id

-id: template id

attach vpc from gateway gateway: gateway id

vpc: vpc id

detach vpc from gateway gateway: gateway id

vpc: vpc id

bu netaas listeners   (listener service management)

bu netaas listeners add create listener name: listener name

account: parent account id

traffic_type: incoming traffic profile; one of: ['tcp', 'http', 'ssl

passthrough', 'https-offloading', 'https-end-to-end']

-desc: listener description

-persistence: persistence type: ['sourceip', 'cookie', 'ssl-sessionid']

-cookie_name: cookie name

-cookie_mode: cookie mode: ['insert', 'prefix', 'app-session']

-expire: expire time in seconds

-client_cert_path: client certificate path

-server_cert_path: server certificate path

-client_cipher: cipher suite used by client; one of: ['DEFAULT',

'ECDHE-RSA-AES128-GCM-SHA256', 'ECDHE-RSA-AES256-GCM

SHA384', 'ECDHE-RSA-AES256-SHA', 'ECDHE-ECDSA-AES256-SHA',

'ECDH-ECDSA-AES256-SHA', 'ECDH-RSA-AES256-SHA', 'AES256-

SHA', 'AES128-SHA', 'DES-CBC3-SHA']

-server_cipher: cipher suite used by server; one of: ['DEFAULT',

'ECDHE-RSA-AES128-GCM-SHA256', 'ECDHE-RSA-AES256-GCM

SHA384', 'ECDHE-RSA-AES256-SHA', 'ECDHE-ECDSA-AES256-SHA',

'ECDH-ECDSA-AES256-SHA', 'ECDH-RSA-AES256-SHA', 'AES256-

SHA', 'AES128-SHA', 'DES-CBC3-SHA']

-insert_x_forwarded_for: insert X-Forwarded-For HTTP header

-redirect_to: url to redirect client requests

bu netaas listeners delete delete listeners ids: comma separated
listener ids

bu netaas listeners get get listener id: listener uuid or name

bu netaas listeners list list listeners -accounts: list of comma
separated account ids -ids: list of comma separated listener ids

-tags: list of comma separated tags

-page: list page [default=0]

-size: list page size [default=20]

bu netaas listeners templates

get listener templates account: account id -id: template id

bu netaas listeners update update listener id: listener id

-desc: listener description

-persistence: persistence type: ['sourceip', 'cookie', 'ssl-sessionid']

-cookie_name: cookie name

-cookie_mode: cookie mode: ['insert', 'prefix', 'app-session']

-expire: expire time in seconds

-insert_x_forwarded_for: insert X-Forwarded-For HTTP header, ['True',

'False']

-redirect_to: url to redirect client requests

bu netaas load-balancers   (load balancer service management)

bu netaas load-balancers add

create load balancer name: load balancer name

account: parent account id

template: load balancer service definition

protocol: protocol for connections to load balancer: ['http', 'https']

port: port number

bu netaas load-balancers delete

bu netaas load-balancers delete-predefined-service

bu netaas load-balancers get

bu netaas load-balancers list

bu netaas load-balancers start

bu netaas load-balancers stop

bu netaas load-balancers templates

bu netaas load-balancers update

listener: listener id

target_group: target group id

-desc: load balancer description

-static_ip: load balancer frontend ip address

-max_conn: maximum concurrent connections

-max_conn_rate: maximum connections per second

-deploy_env: project deployment environment: ['prod', 'preprod',

'stage', 'test']

delete load balancer id: load balancer id

delete load balancer generic services account: account id

get load balancer id: load balancer uuid or name

list load balancers -accounts: list of comma separated account ids -ids:
list of comma separated load balancer ids

-tags: list of comma separated tags

-page: list page [default=0]

-size: list page size [default=20]

enable load balancer id: load balancer id

disable load balancer id: load balancer id

get load balancer templates account: account id

-id: template id

update load balancer id: load balancer id

-desc: load balancer description

-protocol: protocol for connections to load balancer: ['http', 'https']

-port: port number

-max_conn: maximum concurrent connections

-max_conn_rate: maximum connections per second

bu netaas securitygroups   (security groups service management)

bu netaas securitygroups add

bu netaas securitygroups add-rule

bu netaas securitygroups del-rule

bu netaas securitygroups delete

bu netaas securitygroups get

bu netaas securitygroups list

bu netaas securitygroups patch

bu netaas securitygroups templates

create a security group name: security group name

vpc: parent vpc

-template: template id

add a security group rule type: egress or ingress. For egress rule the
destination. For ingress rule specify the source

securitygroup: securitygroup id

-proto: protocol. can be tcp, udp, icmp or -1 for all

-port: can be an integer between 0 and 65535 or a range with start

and end in the same interval. Range format is -. Use -1 for all ports.

Set subprotocol if proto is icmp (8 for ping)

-dest: rule destination. Syntax :. Destination type can be SG, CIDR. For

SG value must be . For CIDR value should like 10.102.167.0/24.

-source: rule source. Syntax :. Source type can be SG, CIDR. For SG

value must be . For CIDR value should like 10.102.167.0/24.

delete a security group rule type: egress or ingress. For egress rule
the destination. For ingress rule specify the source

securitygroup: securitygroup id

-proto: protocol. can be tcp, udp, icmp or -1 for all

-port: can be an integer between 0 and 65535 or a range with start

and end in the same interval. Range format is -. Use -1 for all ports.

Set subprotocol if proto is icmp (8 for ping)

-dest: rule destination. Syntax :. Destination type can be SG, CIDR. For

SG value must be . For CIDR value should like 10.102.167.0/24.

-source: rule source. Syntax :. Source type can be SG, CIDR. For SG

value must be . For CIDR value should like 10.102.167.0/24.

delete a security group securitygroup: securitygroup id

get security group with rules securitygroup: securitygroup id

get security groups -accounts: list of account id comma separated -ids:
list of security group id comma separated

-vpcs: list of vpc id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

patch a security group securitygroup: securitygroup id

get security group templates account: account id

-id: template id

bu netaas sshgw   (ssh gateway service management)

bu netaas sshgw conf activate

activate ssh gw configuration id: ssh gateway conf id port: destination
port

bu netaas sshgw conf-add add ssh gateway configuration name:
configuration name

gw_type: ssh gateway type (gw_dbaas,gw_cpaas)

-desc: configuration description

dest_uuid: destination service instance uuid

-allowed_ports: comma separated list of ranges (start-end) or single

ports. e.g. 8000-9000,22

-forbidden_ports: comma separated list of ranges (start-end) or single

ports. e.g. 8000-9000,22

bu netaas sshgw conf-delete delete a ssh gateway configuration id: ssh
gateway conf id

bu netaas sshgw conf-get get ssh gateway configuration id: ssh gateway
configuration id

bu netaas sshgw conf-list get ssh gateway configurations -accounts: list
of account id comma separated -ids: list of ssh gateway configurations
id comma separated

-names: list of ssh gateway configurations names comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu netaas subnets   (vpc subnet service management)

bu netaas subnets add add virtual private cloud subnet name: subnet name

vpc: vpc id

cidr_block: subnet cidr block

zone: availability zone

-template: subnet template

bu netaas subnets delete delete a subnet subnet: subnet id

bu netaas subnets list get vpc subnets -accounts: list of account id
comma separated -ids: list of subnet id comma separated

-vpcs: list of vpc id comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu netaas subnets templates

get vpc templates account: account id -id: template id

bu netaas target-groups   (target group service management)

bu netaas target-groups add

bu netaas target-groups delete

create empty target group name: target group name

account: parent account id

balancing_algorithm: algorithm used to load balance targets: ['round

robin', 'ip-hash', 'leastconn', 'uri']

target_type: target type: ['vm', 'container']

-desc: target group description

-health_monitor: id of the custom monitor to perform health checks on

targets

-transparent: whether client IP addresses are visible to the backend

servers, [True, False]

delete target groups ids: comma separated target group ids

bu netaas target-groups get get target group id: target group uuid or
name

bu netaas target-groups health-monitor-deregister

deregister health monitor from target group

id: target group id

bu netaas target-groups health-monitor-register

register health monitor with target group id: target group id monitor:
health monitor id

bu netaas target-groups list list target groups -accounts: list of comma
separated account ids -ids: list of comma separated target group ids

-tags: list of comma separated tags

-page: list page [default=0]

-size: list page size [default=20]

bu netaas target-groups targets-deregister

bu netaas target-groups targets-register

bu netaas target-groups templates

deregister targets from target group id: target group id

targets: comma separated list of target ids

register targets with target group id: target group id

targets: comma separated list of couples : or triplets ::

get target group templates account: account id

-id: template id

bu netaas target-groups update

update target group id: target group id

-desc: target group description

-balancing_algorithm: algorithm used to load balance targets: ['round

robin', 'ip-hash', 'leastconn', 'uri']

-transparent: whether client IP addresses are visible to the backend

servers, [True, False]

bu netaas vpcs   (virtual private cloud network service management)

bu netaas vpcs add add virtual private cloud name: vpc name

account: account id

cidr_block: vpc cidr block

-template: vpc template

-tenancy: allowed tenancy of instances launched into the VPC. Use

default for shared vpc. Use dedicated for private vpc. default is

dedicated

bu netaas vpcs delete delete a vpc vpc: vpc id

bu netaas vpcs list get private cloud networks -accounts: list of
account id comma separated -ids: list of private cloud network id comma
separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu netaas vpcs templates get vpc templates account: account id

-id: template id

bu orgs   (organization management)

bu orgs active-services get organization active services info id:
organization uuid or name

bu orgs add add organization name: organization name

-desc: organization description

-attrib: organization attributes

orgtype: organization type

-hasvat: organization hasvat

-ext-anag-id: organization ext_anag_id

-partner: organization partner

-referent: organization referent

-email: organization email

-legalemail: organization legalemail

-postaladdress: organization legalemail

bu orgs delete delete organization id: organization uuid or name

bu orgs get get organizations -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: organization uuid

-objid: authorization id

-name: organization name

-org-type: organization type

-ext-anag-id: organization ext_anag_id

-attributes: organization attributes

-hasvat: organization hasvat

-partner: organization partner

-referent: organization referent

-email: organization email

-legalemail: organization legalemail

-postaladdress: organization legalemail

bu orgs refresh refresh organization id: organization uuid or name

bu orgs update update organization name: organization name

-desc: organization description

-attrib: organization attributes

org-type: organization type

-hasvat: organization hasvat

-ext-anag-id: organization ext_anag_id

-partner: organization partner

-referent: organization referent

-email: organization email

-legalemail: organization legalemail

-postaladdress: organization legalemail

bu orgs-auth   (organization authorization)

bu orgs-auth group-add add organization role to a group id: organization
uuid role: organization role

group: authorization group

bu orgs-auth group-del remove organization role from a group id:
organization uuid role: organization role

group: authorization group

bu orgs-auth group-get get organization groups id: organization uuid bu
orgs-auth role-get get organization roles id: organization uuid

bu orgs-auth user-add add organization role to a user id: organization
uuid role: organization role

user: authorization user

bu orgs-auth user-del remove organization role from a user id:
organization uuid role: organization role

user: authorization user

bu orgs-auth user-get get organization users id: organization uuid

bu service-catalogs   (service catalog management)

bu service-catalogs add add service catalog name: service catalog name
-desc: service catalog description

bu service-catalogs definition-add

bu service-catalogs definition-del

delete service catalog service definition id: service catalog id

definitions: comma separated list of definition id

delete service catalog service definition id: service catalog id

definitions: comma separated list of definition id

bu service-catalogs delete delete service catalog id: service catalog id

bu service-catalogs get get srvcatalogs -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: service catalog id

-objid: authorization id

-name: service catalog name

bu service-catalogs patch refresh service catalog id: service catalog id

bu service-catalogs update update service catalog id: service catalog id
-name: service catalog name

-desc: service catalog description

bu service-catalogs-auth   (service catalog authorization)

bu service-catalogs-auth group-add

bu service-catalogs-auth group-del

bu service-catalogs-auth group-get

bu service-catalogs-auth role-get

bu service-catalogs-auth user-add

bu service-catalogs-auth user-del

bu service-catalogs-auth user-get

add service catalog role to a group id: service catalog id role: service
catalog role

group: authorization group

remove service catalog role from a group id: service catalog id role:
service catalog role

group: authorization group

get service catalog groups id: service catalog id get service catalog
roles id: service catalog id

add service catalog role to a user id: service catalog id role: service
catalog role

user: authorization user

remove service catalog role from a user id: service catalog id role:
service catalog role

user: authorization user

get service catalog users id: service catalog id

bu service-consumes   (service consume management)

bu service-consumes aggregate

generate aggregated consume period: aggregation period. Ex. YYYY-MM o
YYYY-MM-GG

bu service-consumes get list service job schedule -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: consume id

-type: consume type id

-account: account id

-aggr_type: aggregation type

-period: aggregation period

-task: execution task

-date_start: start date

-date_end: stop date

bu service-defs   (service definition management)

bu service-defs add add service definition name: service definition name
type: service type id

params: service definition params

-desc: service definition description

-version: service definition version

-status: service definition status

bu service-defs delete delete service definition id: service definition
id

bu service-defs get get service definitions -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-name: entity name

-objid: authorization id

-version: definition version

-status: type status

bu service-defs update update service definition id: service definition
id

-name: service definition name

-desc: service definition description

-status: service definition status

-config: service definition config key:value

bu service-insts   (service instance management)

bu service-insts check check service instance -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

bu service-insts config-set update resource entity config id: resource
entity id

key: config key like config.key

-value: config value

bu service-insts delete delete service instance -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

-propagate: if True propagate delete to all cmp modules

[default=false]

-force: if True force delete [default=false]

bu service-insts filter get service instances user_name: user name

bu service-insts get get service instances -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-legacy: use legacy v1

-name: entity name

-objid: authorization id

-version: definition version

-status: type status

-account: account id

-resource: resource uuid

-parent: parent service instance

-plugintype: service plugintype

-tags: comma separated tag list

-iscontainer: if True show only container service instance

bu service-insts import from-resource

import service instance from resource name: service instance name -desc:
service instance description

account: account id

plugintype: plugin type of the service instance

container_plugintype: plugin type of the container

-service_definition_id: service definition id

resource: resource id

-parent: parent service instance id

bu service-insts patch patch service instance -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

bu service-insts status update service instance status -size: list page
size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

status: service instance status

bu service-insts tag-add add tag to service instance -size: list page
size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

tags: comma separated list of tags

bu service-insts tag-del delete tag from service instance -size: list
page size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

tags: comma separated list of tags

bu service-insts tag-get get tag of service instance id: service
instance id

bu service-insts update update service instance -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: service instance id

-resource_uuid: resource uuid

-parent: parent service instance

-name: service instance name

bu service-links   (service link management)

bu service-links add add service link name: service link name account:
account id

type: service link type

start_service: start service uuid

end_service: end service uuid

-attributes: service link attributes

bu service-links delete delete service links ids: comma separated
service link uuids -force: if true force the delete

bu service-links get list service links -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: link uuid

-name: link name

-service: start or end service uuid

-type: link type

-objid: link authorization id

-tags: link tags

bu service-links tag-add add tag to service link id: service link id
tag: tag

bu service-links tag-del delete tag from service link id: service link
id tag: tag

bu service-links tag-get get tag of service link id: service link id

bu service-links update update service link id: service link uuid -name:
service link name

-type: service link type

-start_service: start service uuid

-end_service: end service uuid

-attributes: service link attributes

bu service-metrics   (service metric management)

bu service-metrics acquire acquire metric -account: account id -type:
metric type

-service: metric service instance id

bu service-metrics get list service metrics -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: metric id

-day: sample day

-value: metric value

-num: metric num

-service: metric service instance id

-type: metric type

-jobid: sample job id

bu service-metrics type-add add service metric type name: metric type
name

-desc: metric type description

-group: metric type group

type: metric type. Supported values:

CONSUME|BUNDLE|OPT_BUNDLE|PROF_SERVICE

-unit: metric type unit

-status: metric type status

-active: metric type active

-limits: json file with limit definition.Ex. {"limits" : [{ "name" :

"LimitCPU", "desc" : "LimitCPU", "value": 2.0, "metric_type_id" : "1"

}]}

bu service-metrics type delete

delete service metric types -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: metric type id

bu service-metrics type-get list service metric types -size: list page
size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: metric type id

-name: metric type name

-group: metric type group name

-type: metric type

bu service-metrics type update

update service metric type -id: metric type id

-name: metric type name

-desc: metric type description

-group: metric type group

-type: metric type. Supported values:

CONSUME|BUNDLE|OPT_BUNDLE|PROF_SERVICE

-unit: metric type unit

-status: metric type status

-active: metric type active

-limits: json file with limit definition.Ex. {"limits" : [{ "name" :

"LimitCPU", "desc" : "LimitCPU", "value": 2.0, "metric_type_id" : "1"

}]}

bu service-schedules   (service schedule management)

bu service-schedules add add service job schedule config: job schedule
config file

bu service-schedules add example

list service job schedule

bu service-schedules delete delete service job schedule -id: job
schedule id

bu service-schedules get list service job schedule -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: job schedule id

-name: job schedule name

-job_name: job schedule job name

-job_id: job schedule job id

-type: job schedule type

-metric_type: job schedule metric type

bu service-schedules restart restart service job schedule -id: job
schedule id bu service-schedules start start service job schedule -id:
job schedule id bu service-schedules stop stop service job schedule -id:
job schedule id

bu service-tags   (service tag management)

bu service-tags add add service tag value: service tag value account:
account id

bu service-tags delete delete service tags ids: comma separated service
tag id -force: if true force the delete

bu service-tags get list service tags -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-value: tag value

-service: service id

-link: service link id

bu service-tags update update service tag id: service tag uuid -value:
service tag value

bu service-types   (service type management)

bu service-types add add service type name: service type name objclass:
python class full path

-version: service type version

-flag_container: if True service is a container

-status: service type status

bu service-types delete delete service type ids: service type id

bu service-types get get service types -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-name: entity name

-objid: authorization id

-version: type version

-status: type status

bu service-types plugin-get get service type plugins -size: list page
size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

bu service-types process get

get service type process id: service type id

bu service-types process-set set service type process id: service type
id

method: service type process method

-name: name

-desc: description

-process: process

-template: template file

bu service-types update update service type id: service type id

-name: service type name

-objclass: python class full path

-version: service type version

-flag_container: if True service is a container

-status: service type status

bu staas   (storage service management)

bu staas info get storage service info account: account id

bu staas quotas get storage service quotas account: account id

bu staas efs   (file share service management)

bu staas efs add create a share name: share name

account: parent account id

size: share size

-type: share type

-mode: share performance mode. Can be generalPurpose or

localPurpose

bu staas efs delete delete a share share: share id

bu staas efs get get share share: share id

bu staas efs grant-add create a share grant share: share id

access_level: access to grant shld be rw \| r

access_type: access type should be ip

access_to: access to expression

bu staas efs grant-delete delete share grant share: share id

grant: grant id

bu staas efs list list share -accounts: list of account id comma
separated -name: list of share id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu staas efs resize resize a share share: share id

size: new share size in GB

bu staas efs target-add create share mount target share: share id

subnet: share subnet

protocol: protocol should be nfs|cifs

-label: custom label to be used when you want to use a labelled share

type

-ontap_volume: ontap netapp volume id

bu staas efs target-delete delete share mount target share: share id

bu staas efs target-list list share mount target -accounts: list of
account id comma separated -name: list of share id comma separated

-tags: list of tag comma separated

-page: list page [default=0]

-size: list page size [default=20]

bu staas efs types get share types

catalogs   (api catalog management)

catalogs add add catalog name: catalog name

zone: catalog zone

catalogs add-endpoint add catalog endpoint name: catalog endpoint name

catalog: catalog uuid

service: service name like auth or resource

uri: service uri

catalogs delete delete catalog id: catalog uuid

catalogs delete-endpoint delete catalog endpoint id: catalog endpoint
uuid

catalogs get get catalogs -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: catalog uuid

catalogs get-endpoints get catalog endpoints -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: catalog endpoint uuid

catalogs ping-endpoint ping catalog endpoint id: catalog endpoint uuid

catalogs ping-endpoints ping catalog endpoints id: catalog uuid

dq-res   (resource data quality)

dq-res dq-entities   (entities data quality)

dq-res dq-entities bad-get get bad resources -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-definition: entity definition

dq-res dq-entities bad remove

get bad resources -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: entity id

dq-res dq-entities check check resource entities -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-name: entity name

-desc: entity description

dq-res dq-entities check compute-instance

dq-res dq-entities compute volume-check

dq-res dq-entities compute volume-repair

-container: container uuid or name

-type: entity type

-objid: entity authorization id

-ext_id: entity physical id

-parent: entity parent

-state: entity state

-attributes: entity attributes

-tags: entity tags

check compute instance -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-hypervisor: hypervisor

-name: name filter

repair compute volume tree -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-definition: entity definition

repair compute volume tree -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-definition: entity definition

dq-res dq-entities remove remove bad resource -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: entity id

dq-res dq-links   (links data quality)

dq-res dq-links bad-get get bad links -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-definition: entity definition

dq-res dq-links bad-remove get bad links -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: link id

dq-res dq-links check repair resource links -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: link id

dq-res dq-links remove remove bad link -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: link id

dq-service   (service data quality)

dq-service dq-insts   (service instance data quality)

dq-service dq-insts check check service instances -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-name: entity name

-desc: entity description

-container: container uuid or name

-type: entity type

-objid: entity authorization id

-ext_id: entity physical id

-parent: entity parent

-state: entity state

-attributes: entity attributes

-tags: entity tags

mgmt   (Administration and objects management)

mgmt database   (database administartion commands)

mgmt database check check database storage database: database service id
uuid or name this is one of the serivce identifiers

--tofile: store to file only when format is json or yaml

mgmt loadbalancers   (loadbalancer administration commands)

mgmt loadbalancers delete delete load balancer id: load balancer id

-no-linked-objs: Use this option to avoid deleting service instances
like

target group and custom listener linked to load balancer

-no-physical-resources: Use this option to delete only CMP metadata

without deleting physical resources

mgmt loadbalancers load import load balancer appliance: network
appliance (e.g. nsx edge) uuid -account: the uuid of the account owner
of the virtual server(s) to

import

-virtual-server: the name of the virtual server to import

platform   (platform management)

platform check check platform status -engines: engine name

platform version get platform versions -engine: engine name

platform awx   (awx platform management)

platform awx ad-hoc command-add

platform awx ad-hoc command-get

platform awx ad-hoc command-relaunch

platform awx ad-hoc command-stdout

add add hoc commands -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

inventory: inventory id

credential: credential id

-verbosity: verbosity

get add hoc commands -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-inventory: inventory id

-id: job id

relaunch add hoc command -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

get add hoc command stdout -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

platform awx credential-del delete credential -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: credential id

platform awx credential-get get credentials -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

platform awx credential-git add

platform awx credential ssh-add

platform awx credential type-get

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: credential id

-name: credential name

add git credential -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: credential name

organization: organization id

username: username

password: password

add ssh credential -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: credential name

organization: organization id

username: username

-password: password

-key_data: ssh key data file

-key_unlock: ssh key unlock

-become: become method

get credential types -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: credential type id

platform awx host-add add host -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: host name

inventory: inventory id

-desc: host description

-vars: host variables. ex: k1:v1,k2:v2

platform awx host-del delete host -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: host id

platform awx host-get get hosts -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: host id

-name: host name

platform awx host-group add

platform awx host-group del

add group to host -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: host id

group: group id

remove group from host -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: host id

group: group id

platform awx inventory-add add inventory -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: inventory name

organization: organization id

platform awx inventory-del delete inventory -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: inventory id

platform awx inventory-get get inventories -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: inventory id

-name: inventory name

platform awx inventory group-add

platform awx inventory group-del

platform awx inventory group-get

platform awx inventory host-get

platform awx inventory script-add

platform awx inventory script-del

platform awx inventory script-get

platform awx inventory source-sync

platform awx job-event error-get

add inventory group -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

inventory: inventory id

name: inventory group name

-desc: host description

-vars: host variables. ex: k1:v1,k2:v2

delete inventory group -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: inventory group id

get inventory groups -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: inventory group id

-name: inventory name

-inventory: inventory id

get inventory hosts -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: inventory group id

-name: inventory name

-inventory: inventory id

add script inventory -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: script inventory name

organization: organization id

script: script. Ex. #!/bin/bash source /opt/beehive/bin/activate

delete script inventory -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: inventory id

get inventory scripts -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-inventory: inventory id

-id: group id

sync inventory source -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: inventory source id

get job error -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

platform awx job-event-get get job events -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

-query: job event query. Comma separated k:v

platform awx job-get get jobs -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: job id

platform awx job-relaunch relaunch job -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

platform awx job-stdout get job stdout -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: job id

platform awx org-get get organizations -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: organization id

-name: organization name

platform awx ping ping awx -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

platform awx project-add add project -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: project name

organization: organization id

credential: credential id

scm_url: scm url

-scm_type: scm type

-scm_branch: scm branch

-scm_update_on_launch: scm update on launch

platform awx project-del delete project -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: project id

platform awx project-get get projects -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: project id

-name: project name

platform awx project-job event-get

platform awx project-job get

platform awx project-job stdout

get project job events -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: project job id

get project job -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: project job id

get project job stdout -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: project job id

platform awx project-sync sync project -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: project id

platform awx template-add add template -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

name: template name

inventory: inventory id

project: project id

playbook: playbook

-verbosity: verbosity: 0 (Normal) (default), 1 (Verbose), 2 (More

Verbose), 3 (Debug), 4 (Connection Debug), 5 (WinRM Debug)

platform awx template-del delete template -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: template id

platform awx template-get get templates -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

-id: template id

-name: template name

platform awx template launch

launch template -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

id: template id

credentials: comma separated credentials id

-extras: variables used when launching job template, k1:v1;k2:v2

platform awx version get awx version -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: awx platform reference label

platform cmp customize   (cmp customization)

platform cmp customize get get available configurations

platform cmp customize run run customization. This command can be used
many times to add new items

config: config file

-filter: filter to apply ::. Ex.

resource.entities.site_networks:name:NVLP3-Prov-WEB2-test -sections:
comma separated list of section to execute

platform cmp customize show

show configuration config: config file

-filter: filter to apply ::. Ex.

resource.entities.site_networks:name:NVLP3-Prov-WEB2-test

platform cmp logs   (cmp logs management)

platform cmp logs api get api request received -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-index: index name

-id: api request id

-uri: api request ri. uri:method

-user: api request source user

-ip: api request source ip

-sort: sort field. Ex. @timestamp:desc

platform cmp logs engine show log for cmp engine -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-index: index name

-name: container partial name. Ex. uwsgi-auth, worker-auth, uwsgi-ssh

-sort: sort field. Ex. date:desc

-pod: pod name

-op: oepration id. Can be api_id, task_id, task_id:step_name

platform cmp logs event show cmp events -size: list page size
[default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-index: index name

-kvargs: kvargs like query string

-id: event id

-type: event id

-sort: sort field. Ex. date:desc

platform cmp post-install   (DEPRECATED - cmp post install management)

platform cmp post-install get

platform cmp post-install run

get post install available configurations

run post install. This command can be used many times to add new items

config: config file

-filter: filter to apply ::. Ex.

resource.entities.site_networks:name:NVLP3-Prov-WEB2-test -sections:
comma separated list of section to execute

platform cmp post-install show

get post install available configurations config: config file

-filter: filter to apply ::. Ex.

resource.entities.site_networks:name:NVLP3-Prov-WEB2-test

platform cmp subsystems   (cmp subsystems management)

platform cmp subsystems create

platform cmp subsystems deploy

platform cmp subsystems get

platform cmp subsystems redeploy

platform cmp subsystems runtime-api-spec

platform cmp subsystems runtime-apidocs

platform cmp subsystems runtime-capabilities

platform cmp subsystems runtime-get

platform cmp subsystems runtime-log

platform cmp subsystems runtime-ping

platform cmp subsystems runtime-version

create cmp subsystem structure (db, data) subsystem: subsystem. Ex.
resource, service file: subsystem config file full path

deploy cmp subsystem -subsystem: subsystem. Ex. resource, service get
cmp subsystem config -id: subsystem. Ex. resource, service

redeploy cmp subsystem subsystem: subsystem. Ex. resource, service
-path: remote package path

-pkgs: list of package to sync

get cmp instance openapi spec id: subsystem. Ex. resource, service

get cmp instance swagger web interface id: subsystem. Ex. resource,
service

get cmp instance capabilities id: subsystem. Ex. resource, service

get cmp subsystems -id: subsystem. Ex. resource, service

-role: deployment role

get cmp subsystem pod log subsystem: subsystem. e.g. resource, service
role: deployment role. e.g. uwsgi

-follow: follow log. Default: true.

-lines: number of log lines to show. Default: 100. Ignored when follow

is true.

ping cmp subsystems -id: subsystem. Ex. resource, service

-role: deployment role

get cmp instance versions id: subsystem. Ex. resource, service

platform cmp subsystems sync

update cmp nivola python packages - use with devel env

-path: remote package path -pkgs: list of package to sync

platform cmp subsystems undeploy

undeploy cmp subsystem -subsystem: subsystem. Ex. resource, service

platform cmp subsystems update

update cmp subsystem structure (db, data)

subsystem: subsystem. Ex. resource, service file: subsystem config file
full path

platform cmp tests   (cmp test management)

platform cmp tests get list cmp regression tests -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-package: python package

-plan: name of the test plan

-group: name of the sub test group

platform cmp tests run run cmp regression tests -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-package: python package

-plan: name of the test plan

-group: name of the sub test group

-list: list of test id to run

-test: name of test to run

-mainconf: optional main test configuration

-conf: optional extra test configuration

-validate: if True enable api validation in test

-user: user used to run test. Ex. test1, admin [default=test1]

-concurrency: specify how many tests run in parallel for massive test

[default=2]

platform console   (console management)

platform console connect connect to console -C, --console: console label

-user: user name

-pwd: user password required

platform console update update shell console -C, --console: console
label

-pkgs: user name

platform console user-env add

setup user additional environment -C, --console: console label

user_ssh: console user

user_env: comma separated list of environment to add

platform console user-get list user configured -C, --console: console
label user: user name

platform console user-list list user configured -C, --console: console
label

platform console user-setup setup user home directory and configuration

-C, --console: console label user_ssh: console user

platform console user update

update user base config -C, --console: console label user_ssh: console
user

-isadmin: console user

platform console versions get cmp packages version -C, --console:
console label

platform datadomain   (datadomain management)

platform datadomain info info from datadomain

platform datadomain mtree get

platform datadomain

network-get

get datadomain mtrees -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

-mtree_id: data domain mtree id

get datadomain networks -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

-network_id: data domain network id

platform datadomain ping ping datadomain instances -port: datadomain
port

platform datadomain protocol-nfs-add

platform datadomain protocol-nfs-client-add

platform datadomain protocol-nfs-client-del

platform datadomain protocol-nfs-get

add datadomain nfs exports -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

mtree: mtree name

path: data domain nfs export path

add datadomain nfs export client -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

nfs_id: data domain nfs exports id

client: client fqdn

delete datadomain nfs export client -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

nfs_id: data domain nfs exports id

client: client fqdn

get datadomain nfs exports -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

platform datadomain services-get

platform datadomain setting-get

platform datadomain tenant-get

platform datadomain trust get

platform datadomain user get

-nfs_id: data domain nfs exports id

get datadomain services id: data domain system id get datadomain
settings id: data domain system id

get datadomain tenants -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

-tenant_id: data domain tenant id

get datadomain trust -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

get datadomain users -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: data domain system id

-user_id: data domain user id

platform dns   (dns platform)

platform dns ping ping dns -O, --orchestrator: dns platform reference
label -P, --project: dns current project name

platform dns version get dns version -O, --orchestrator: dns platform
reference label -P, --project: dns current project name

platform dns zone-alias query

get fqdn address form alias -O, --orchestrator: dns platform reference
label -P, --project: dns current project name

alias: alias

-group: dns group. Can be resolver or update [default=resolver]

platform dns zone authority-get

the SOA (Start of Authority) used to manage the zone

-O, --orchestrator: dns platform reference label -P, --project: dns
current project name id: zone

platform dns zone-fqdn query

get ip address form fqdn -O, --orchestrator: dns platform reference
label -P, --project: dns current project name

fqdn: fqdn

-group: dns group. Can be resolver or update [default=resolver]

platform dns zone-get get all the managed zones -O, --orchestrator: dns
platform reference label -P, --project: dns current project name

platform dns zone nameserver-get

get all the nameservers that resolve the zone

-O, --orchestrator: dns platform reference label -P, --project: dns
current project name id: zone

platform dns zone orchestrator-get

get all the configured orchestrators -O, --orchestrator: dns platform
reference label -P, --project: dns current project name

platform elastic   (elastic management)

platform elastic cluster health

platform elastic cluster nodes

platform elastic cluster stats

get cluster health get cluster nodes get cluster statistics

platform elastic index-count count index documents -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

index: index name

-query: simple query like field1:value1

-sort: sort field. Ex. date:desc]

-fields: comma separated list of fields to show

platform elastic index-del delete index index: index name

platform elastic index-get get indexes -index: index name -pattern:
index pattern

platform elastic index-list list indexes -pattern: index pattern

platform elastic index-query query index -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

index: index name

-query: simple query like field1:value1

-sort: sort field. Ex. date:desc]

-fields: comma separated list of fields to show

platform elastic index-stats get index statistics index: index name

platform elastic info get elastic info

platform elastic ping ping elastic

platform elastic role mapping-add

platform elastic role mapping-del

platform elastic role mapping-get

add role mapping name: role mapping name role_name: role name

user_email: user email

realm_name: realm name

delete role mapping name: role mapping name get role mapping -name: role
mapping name

platform elastic user-add add user name: user name

password: password

role: role

-full_name: full_name

-email: full_name

platform elastic user-del delete user name: user name

platform elastic user-get get user -name: user name

platform fwlog   (firewall logs management)

platform fwlog dfw show log for dfw -O, --orchestrator: mysql cluster or
single node reference label -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-index: index name

-reject: if true show only reject

-sort: sort field. Ex. @timestamp:desc

-pretty: if true show pretty logs

-ip: ip address

platform fwlog edge show log for edge -O, --orchestrator: mysql cluster
or single node reference label -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

edge: edge name

-type: log type: firewall, config, nat,

-index: index name

-reject: if true show only reject

-sort: sort field. Ex. @timestamp:desc

-pretty: if true show pretty logs

-ip: ip address

platform grafana   (grafana platform management)

platform grafana alert notification-add

platform grafana alert notification-del

platform grafana alert notification-get

add alert notification -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

name: alert notification name

email: alert notification email

delete alert notification -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: alert notification uid

get alert notification -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-id: alert notification uid

-name: alert notification name

platform grafana alert notification-update

platform grafana

dashboard-add

platform grafana

dashboard-copy

platform grafana

dashboard-del

platform grafana

dashboard-get

update alert notification -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: alert notification uid

name: alert notification name

email: alert notification email

add dashboard -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

data_dashboard: dashboard data

copy dashboard -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

name: dashboard name to search

folder_uid: folder uid where add dashboard

organization: organization name

division: division name

account: account name

delete dashboard -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: dashboard id

get dashboard -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-id: dashboard uid

-search: dashboard search query

-folder: folder id - 0 for General

platform grafana folder-add add folder -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

name: folder name

platform grafana folder dashboard-get

get folder dashboard -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: folder uid or "general" for general folder

-search: dashboard search query

platform grafana folder-del delete folder -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

uid: folder uid

platform grafana folder-get get folder -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-uid: folder uid

-name: folder name

platform grafana folder permission-add

add folder permission -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

uid: folder uid

-team_viewer: team id viewer

-team_editor: team id editor

platform grafana folder permission-get

add folder permission -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

uid: folder uid

-team_viewer: team id viewer

-team_editor: team id editor

platform grafana ping ping grafana -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

platform grafana team-add add team -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

name: team name

platform grafana team-del delete team -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: team id

platform grafana team-get get team -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-id: team id

-name: team name

platform grafana team-user add

platform grafana team-user del

platform grafana team-user get

add user to team -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

team_id: team id

user_id: user id

delete user from team -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

team_id: team id

user_id: user id

get user of team -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: team id

platform grafana user-add add user -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-name: user name

-email: email

-login: user login

-password: password

platform grafana user-del delete user -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

id: user id

platform grafana user-get get user -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

-id: user uid

-name: user name

platform grafana version get grafana version -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: grafana platform reference label

platform graphite   (graphite management)

platform graphite vm metric

platform graphite vm metric-highest

platform graphite vm metric-one

get vm metrics ip_address_graphite: ip address graphite pod: pod name

vm: vm name

metrics: metric

function: function

period: period

get vm highest metrics ip_address_graphite: ip address graphite pod: pod
name

metrics: metric

function: function

period: period

get vm one metric ip_address_graphite: ip address graphite pod: pod name

vm: vm name

metrics: metric

function: function

period: period

platform k8s   (k8s management)

platform k8s app-add add k8s app -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

app: app name

platform k8s app-del delete k8s app -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

app: app name

platform k8s app-get query k8s app -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

app: app name

platform k8s cluster-health get cluster health

platform k8s cluster-nodes get cluster nodes

platform k8s cluster-stats get cluster statistics

platform k8s deploy-get get k8s deployment app -C, --cluster: k8s
cluster reference label -N, --namespace: k8s current namespace

-id: deployment app id

platform k8s index-count count index documents -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

index: index name

-query: simple query like field1:value1

-sort: sort field. Ex. date:desc]

-fields: comma separated list of fields to show

platform k8s index-del delete index index: index name

platform k8s index-get get indexes -index: index name -pattern: index
pattern

platform k8s index-list list indexes -pattern: index pattern

platform k8s index-query query index -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

index: index name

-query: simple query like field1:value1

-sort: sort field. Ex. date:desc]

-fields: comma separated list of fields to show

platform k8s index-stats get index statistics index: index name platform
k8s info get elastic info

platform k8s namespace get

get k8s namespace -C, --cluster: k8s cluster reference label -N,
--namespace: k8s current namespace

platform k8s node-get get k8s nodes -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

-id: node id

platform k8s ping ping k8s cluster -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

platform k8s pod-connect connect to k8s pod -C, --cluster: k8s cluster
reference label -N, --namespace: k8s current namespace

id: pod id

-cmd: command to run

platform k8s pod-elk-log count

get k8s pod elk log count -C, --cluster: k8s cluster reference label -N,
--namespace: k8s current namespace

-id: pod id

platform k8s pod-get get k8s pod -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

-id: pod id

platform k8s pod-log get k8s pod -C, --cluster: k8s cluster reference
label -N, --namespace: k8s current namespace

-name: pod name like

-id: pod id

-lines: the number of lines from the end of the logs to show

-follow: follow the log stream of the pod

platform k8s role-mapping add

platform k8s role-mapping del

platform k8s role-mapping get

add role mapping name: role mapping name role_name: role name

user_email: user email

realm_name: realm name

delete role mapping name: role mapping name get role mapping -name: role
mapping name

platform k8s service-get get k8s service -C, --cluster: k8s cluster
reference label -N, --namespace: k8s current namespace

platform k8s user-add add user name: user name

password: password

role: role

-full_name: full_name

-email: full_name

platform k8s user-del delete user name: user name

platform k8s user-get get user -name: user name

platform kibana   (kibana platform management)

platform kibana ping ping kibana -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

platform kibana role-add add role -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

name: role name

indice: indice

space_id: space_id

platform kibana role-del delete role -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

name: role name

platform kibana role-get get role -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

-name: role name

platform kibana space-add add space -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

id: space id

name: space name

-description: space description

-color: space color

-initials: space initials

platform kibana space-del delete space -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

id: space id

platform kibana space-get get space -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

-id: space id

platform kibana version get kibana version -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: kibana platform reference label

platform mysql   (mysql/mariadb management)

platform mysql binary-log purge

platform mysql binary-log show

purge mysql binary logs -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

show mysql binary logs -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

platform mysql drop drop mysql db -O, --orchestrator: mysql cluster or
single node reference label db: db name

-port: mysql port

platform mysql drops drop mysql dbs -O, --orchestrator: mysql cluster or
single node reference label dbs: db name comma separated

-port: mysql port

platform mysql dump dump mysql db -O, --orchestrator: mysql cluster or
single node reference label db: db name

file: dump file

platform mysql galera cluster-status

get mariadb galera cluster status -O, --orchestrator: mysql cluster or
single node reference label -port: mysql port

-check_host: list of comma separated host to check

platform mysql load load mysql db -O, --orchestrator: mysql cluster or
single node reference label db: db name

file: dump file

platform mysql ping ping mysql instance -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

platform mysql replica slave-start

platform mysql replica slave-status

platform mysql replica slave-stop

start replica on slave -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

get mariadb slave replica status -O, --orchestrator: mysql cluster or
single node reference label -port: mysql port

stop replica on slave -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

platform mysql dbs   (mysql database management)

platform mysql dbs add add mysql database -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

name: database name

platform mysql dbs drop delete mysql database -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

name: database name

platform mysql dbs get get mysql database list -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

platform mysql dbusers   (mysql user management)

platform mysql dbusers add add mysql user -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

-host: user host

platform mysql dbusers drop

name: user name

pwd: user password

delete mysql user -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

name: user name

platform mysql dbusers get get mysql user list -O, --orchestrator: mysql
cluster or single node reference label -port: mysql port

platform mysql dbusers grant

grant db to user -O, --orchestrator: mysql cluster or single node
reference label -port: mysql port

-host: user host

name: user name

-db: db to grant

platform mysql tables   (mysql table management)

platform mysql tables check check mysql tables -O, --orchestrator: mysql
cluster or single node reference label db: db name

-port: mysql port

platform mysql tables desc get mysql table description -O,
--orchestrator: mysql cluster or single node reference label db: db name

table: table name

-port: mysql port

platform mysql tables get get mysql table list -O, --orchestrator: mysql
cluster or single node reference label db: db name

-port: mysql port

platform mysql tables query query mysql db table -O, --orchestrator:
mysql cluster or single node reference label db: db name

table: table name

-rows: query rows number

-offset: query rows offset

-detail: rotate record output

-fields: comma separated list of fields

-order: ield used to order records

-where: custom where

-port: mysql port

platform nginx   (Nginx management)

platform nginx ping ping nginx instances -O, --orchestrator: mysql
cluster or single node reference label platform nginx status get nginx
instances status -O, --orchestrator: mysql cluster or single node
reference label

platform ontap   (netapp ontap management)

platform ontap cluster-get cluster get -O, --orchestrator: ontap
platform reference label

platform ontap cluster-peer get

cluster peer get -O, --orchestrator: ontap platform reference label

platform ontap ping ping ontap -O, --orchestrator: ontap platform
reference label

platform ontap snapmirror get

get ontap snapmirror volumes -O, --orchestrator: ontap platform
reference label -id: svm uuid

-source_path: source path

-source_svm: source svm

-dest_path: dest path

platform ontap svm-get get svm -O, --orchestrator: ontap platform
reference label -id: svm uuid

-name: svm name like

-order_by: order by

platform ontap svm-peer get

svm get peer -O, --orchestrator: ontap platform reference label -id: svm
uuid

-svm: svm name

-name: name like

-order_by: order by

platform ontap volume-get get volume -O, --orchestrator: ontap platform
reference label -id: volume uuid

-name: volume name like

-svm: svm name to limit the search to (volumes 'in that svm')

-H: human readable (i.e. B, KB, MB, GB, TB)

-precise: show also size as precise integer multiple of bytes

platform ontap volume snapshot-get

platform ontap volume usage

get ontap volume snapshots -O, --orchestrator: ontap platform reference
label volume: volume uuid

get ontap volume usage -O, --orchestrator: ontap platform reference
label svms: comma separated list of svms

-H: human readable (i.e. B, KB, MB, GB, TB)

-precise: show also size as precise integer multiple of bytes

platform openstack   (openstack platform)

platform openstack

aggregate-add

platform openstack

aggregate-del

platform openstack

aggregate-get

platform openstack

aggregate-host-add

platform openstack

aggregate-host-del

platform openstack

aggregate-metadat-update

platform openstack

aggregate-update

add aggregate -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

name: aggregate name

availability_zone: availability zone

delete openstack aggregate -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: aggregate id

get aggregates -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: aggregate id

add host to openstack aggregate -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: aggregate id

host: host_id

delete host from openstack aggregate -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: aggregate id

host: host_id

update metadata to openstack aggregate -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: aggregate id

metadata: key:value,key:value

update openstack aggregate -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: aggregate id

-name: aggregate name

-availability_zone: aggregate availability zone

platform openstack catalog get openstack keystone catalog -O,
--orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform openstack domain get

platform openstack flavor add

platform openstack flavor del

platform openstack flavor extra-spec-add

platform openstack flavor extra-spec-del

platform openstack flavor extra-spec-get

platform openstack flavor extra-spec-update

platform openstack flavor get

get domains -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: cluster id

add flavor -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

name: flavor name

vcpu: vcpu

ram: ram

disk: disk

delete openstack flavor -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

add flavor extra spec -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

spec: flavor extra spec keys. Syntax k1:v1,k2:v2

delete openstack flavor -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

spec: flavor extra spec key

get flavor extra specs -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

-spec: flavor extra spec key

update openstack flavor -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

spec: flavor extra spec key. Syntax k1:v1

spec_value: flavor extra spec key

get flavors -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: flavor id

platform openstack flavor update

platform openstack

floatingip-del

platform openstack

floatingip-get

platform openstack host status

platform openstack image add

platform openstack image del

platform openstack image download

platform openstack image get

platform openstack image schema-get

platform openstack image task-get

platform openstack image upload

platform openstack keypair del

platform openstack keypair get

platform openstack

keystone-role-get

platform openstack

keystone-user-get

platform openstack

mariadb-cluster-status

platform openstack

mariadb-ping

platform openstack

network-add

platform openstack

network-del

update openstack flavor -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: flavor id

-name: flavor name

-desc: flavor description

delete openstack floatingip -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: floatingip id

get floatingips -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: floatingip id

print host status -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-host: node name

-loop: if value > 1 enable query loop

add openstack image -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: image name

-disk_format: disk format e.g.: ami, ari, aki, vhd, vhdx, vmdk, raw,

qcow2, vdi, ploop, iso

-min_disk: amount of disk space in GB that is required to boot the

image.

-min_ram: amount of RAM in MB that is required to boot the image

-visibility: image visibility: public, private, shared, or community

delete openstack image -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: image id

download openstack image -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: image id

name: image file name

get images -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: image id

-owner: owner

-visibility: image visibility: all, public, private, shared, or
community

get image schemas -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: image id

get image tasks -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: image task id

upload openstack image -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: image id

name: image file name

delete openstack keypair -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: keypair id

get keypairs -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: keypair id

get keystone roles -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get keystone users -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get mariadb galera cluster status -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

ping mariadb instances -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

add openstack network -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: network name

project: parent project id

-physical_network: physical network

-segmentation_id: segmentation id

-type: network type. Can be flat, vlan, vxlan, or gre

-mt: the maximum transmission unit MTU

delete openstack network -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: network id

platform openstack network-get

platform openstack network-update

get networks -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: network id

update openstack network -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: network id

-name: network name

-shared: network shared

-mtu: network mtu

platform openstack ping ping openstack -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

platform openstack port add

platform openstack port add-batch

add openstack port -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: port name

network: network id

-subnet: subnet id

-tenant: tenant id

-ipaddress: ip addresses associated to subnet

-allowed-ipaddress: allowed ip address

-allowed-macaddress: allowed ip macaddress

-host: host id

-device_owner: device owner

-security_groups: One or more security group id.

add openstack port -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

platform openstack port-del delete openstack port -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

id: port id

platform openstack port-get get ports -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

-id: port id

-project: project id

-network: network id

-status: the port status. Value is ACTIVE or DOWN

-device: the id of the device that uses this port

-device_owner: the entity type that uses this port. For example: -

compute:nova (server instance), network:dhcp (DHCP agent) -

network:router_interface (router interface).

-security_group: the id of any attached security groups

platform openstack port update

platform openstack project add

platform openstack project default-member-set

platform openstack project del

platform openstack project get

platform openstack project member-get

platform openstack project quota-get

platform openstack project quota-set

update openstack port -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: port id

-name: port name

-desc: port description

-sgs: port security groups comma separated

-allowed_ips: a comma separated list of allowed ip address

-port_security_enabled: enable or disable port security

add openstack project -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: project name

domain: project domain id

-desc: project description

-parent: parent project id

-enabled: enabled status

get openstack project default members -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: project id

delete openstack project -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: project id

get projects -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: project id

get openstack project members -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: project id

get project quotas -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: project id

set project quotas -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: project id

quota_type: project quota type. can be compute, block, network, share

quota: project quota name

value: project quota value

platform openstack project update

platform openstack region get

platform openstack router add

platform openstack router del

platform openstack router get

platform openstack router port-add

platform openstack router port-del

platform openstack router reset-routes

platform openstack router rewrite-routes

platform openstack router update

platform openstack

security-group-add

platform openstack

security-group-check

platform openstack

security-group-del

platform openstack

security-group-get

platform openstack

security-group-rule-add

platform openstack

security-group-rule-del

update openstack project -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: project id

-name: project name

-desc: project description

-domain: parent domain id

-parent: parent project id

-enabled: enabled status

get regions -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

add openstack router -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: router name

tenant: parent project id

-network: physical router

-ext-subnet: external subnet

-ext-ip: external ip address

delete openstack router -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: router id

get routers -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: router id

add openstack router internal interfafe -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: router id

subnet: subnet id

-ip: intarface ip

delete openstack router internal interfafe -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: router id

subnet: subnet id

reset openstack router routes -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: router id

rewrite existing openstack router routes -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: router id

update openstack router -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: router id

-name: router name

-network: physical router

-ext-subnet: external subnet

-ext-ip: external ip address

-routes: routes like dest:nexthop,dest:nexthop

add openstack security group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

name: security_group name

project: parent project id

check openstack security_group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-delete: security_group id

delete openstack security_group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: security_group id

get security_groups -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: security_group id

add openstack security group rule -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: security group rule id

-direction: direction. Can be ingress or egress

-ethertype: Must be IPv4 or IPv6

-port_min: port range min

-port_max: port range max

-protocol: protocol

-remote_ip: remote ip

delete openstack security group rule -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: security group rule id

platform openstack

security-group-rule-get

platform openstack

security-group-update

platform openstack server action-get

platform openstack server add

platform openstack server console

platform openstack server console-output

platform openstack server create-image

platform openstack server del

platform openstack server diagnostics

platform openstack server get

platform openstack server group-add

platform openstack server group-del

platform openstack server group-get

platform openstack server group-member-add

platform openstack server group-member-del

get openstack security group rule -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: security group rule id

update openstack security group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: security_group id

-name: security_group name

-desc: security_group description

get server actions -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: server id

-action: action id

add openstack server -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: server name

-flavor: flavor reference id

-boot_volume: boot volume id

-admin_pass: admin password

-description: description

-security_groups: security groups

-networks: list of networks

-config_drive: list of networks

-availability_zone: availability zone

-image: The UUID of the image to use for your server instance.

get openstack server console -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

get openstack server console output -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: server id

create image from a server -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

name: image name

delete openstack server -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: server id

get openstack server diagnostics -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

get servers -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: server id

-host: compute node name

-status: server status

-updated_at: Filter the server list result by a date and time stamp

when the instance was updated. The date and timestamp format is ISO

8601: CCYY-MM-DDThh:mm:ss±hh:mm. For example,

2015-08-27T09:49:58-05:00

add openstack server group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

name: server group name

-policy: one policy name to associate with the server group. Policy

names are: "anti-affinity" servers in this group must be scheduled to

different hosts, "affinity" servers in this group must be scheduled to

the same host, "soft-anti-affinity" servers in this group should be

scheduled to different hosts if possible, but if not possible then they

should still be scheduled instead of resulting in a build failure, "soft

affinity" servers in this group should be scheduled to the same host if

possible, but if not possible then they should still be scheduled
instead

of resulting in a build failure

delete openstack server group -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server group id

get server groups -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: server group id

-size: number of item to return

-page: page to return

add openstack server group member -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server group id

server: server id

delete openstack server group member -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: server group id

platform openstack server lock

platform openstack server metadata-add

platform openstack server metadata-del

platform openstack server metadata-get

platform openstack server migrate

platform openstack server migration-del

platform openstack server migration-list

platform openstack server pause

platform openstack server port-add

platform openstack server port-del

platform openstack server port-get

platform openstack server reboot

platform openstack server rebuild

platform openstack server reset-state

platform openstack server resize

platform openstack server resume

platform openstack server sg-add

platform openstack server sg-del

server: server id

lock server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

add openstack server metadata -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

volume: volume id

delete openstack server metadata -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

volume: volume id

get openstack server metadata -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

migrate server -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: server id

-host: host id

-live: if true enable live migration

abort server migration -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: server id

migration_id: server migration id

server migration list -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: server id

pause server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

add openstack server port -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

-port: port id

-net: network id

-ipaddress: ip address

-subnet: subnet id

delete openstack server port -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

port: port id

get openstack server ports -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

reboot server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

rebuild openstack server -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

-image: The UUID of the image to use for your server instance.

reset server state -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: server id

state: server state

set server flavor -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: server id

flavor: flavor id

resume server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

add openstack server security group -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: server id

sg: security group id

delete openstack server security group -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: server id

sg: security group id

platform openstack server- get openstack server security group -O,
--orchestrator: openstack platform reference label

sg-get -P, --project: openstack current project name id: server id

platform openstack server smart-ping

platform openstack server smart-reset-status

platform openstack server smart-start

platform openstack server start

platform openstack server stop

platform openstack server suspend

platform openstack server unlock

platform openstack server unpause

platform openstack server update

platform openstack server volume-add

platform openstack server volume-del

platform openstack server volume-get

platform openstack servers migrate

platform openstack share add

platform openstack share del

platform openstack share get

platform openstack share grant-add

ping servers for a host -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-host: node name

-name: vm name

reset servers state for a host -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-host: node name

start servers for a host -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-host: node name

start server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

stop server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

suspend server -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: server id

unlock server -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: server id

unpause server -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: server id

update openstack server -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: server id

-name: server name

-desc: server description

add openstack server volume -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

server_id: server id

volume_id: volume id (see volume-add to create it.)

delete openstack server volume -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

volume: volume id

get openstack server volumes -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: server id

migrate servers -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

from_host: starting host

-to_host: destination host

-live: if true enable live migration

add manila share -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

name: share name

size: share size in GB

proto: share protocol (NFS, CIFS, GlusterFS, HDFS, or CephFS.

CephFS)

type: share type id

-snapshot: share snapshot id

-group: share group id

-network: the id of a share network where the share server exists or

will be created. If is None and you provide a snapshot_id, the network

value from the snapshot is used

delete manila shares -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: share id

-force: if true force delete

get manila shares -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: share id

add manila share access grant -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

-level: the access level to the share. rw: Read and write (RW) access.

ro: Read-only (RO) access.

-type: the access rule type. ip: Authenticates an instance through its
IP

platform openstack share grant-remove

platform openstack share limit-get

platform openstack share message-get

platform openstack share network-add

platform openstack share network-del

platform openstack share network-get

platform openstack share network-security-service add

address. cert: Authenticates an instance through a TLS certificate.

user: Authenticates by a user or group name.

-to: the value that defines the access. ip: A valid format is

XX.XX.XX.XX or XX.XX.XX.XX/XX. For example 0.0.0.0/0. cert: Specify

the TLS identity as the IDENTKEY. A valid value is any string up to 64

characters long in the common name (CN) of the certificate. The

meaning of a string depends on its interpretation. user: A valid value

is an alphanumeric string that can contain some special characters

and is from 4 to 32 characters long.

remove manila share access grant -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

access_id: grant id

get manila share limits -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get manila share messages -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-id: share id

add manila share network -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

name: share network name

-desc: share network description

network: The UUID of a neutron network when setting up or updating

a share network subnet with neutron. Specify both a neutron network

and a neutron subnet that belongs to that neutron network.

subnet: The UUID of the neutron subnet when setting up or updating

a share network subnet with neutron. Specify both a neutron network

and a neutron subnet that belongs to that neutron network.

-availability_zone: The UUID or name of an availability zone for the

share network subnet.

delete manila share networks -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share network id

get manila share networks -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-id: share network id

-network: neutron network id

-subnet: neutron subnet id

add security service to share network -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

id: share network id

service: security service id

platform openstack share network-security-service del

delete security service from share network

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name id: share network id

service: security service id

platform openstack share network-update

platform openstack share server-del

platform openstack share server-get

platform openstack share size-extend

platform openstack share size-shrink

platform openstack share snapshot-revert

update manila share network -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-id: share network id

-name: share network name

-desc: share network description

-network: The UUID of a neutron network when setting up or updating

a share network subnet with neutron. Specify both a neutron network

and a neutron subnet that belongs to that neutron network.

-subnet: The UUID of the neutron subnet when setting up or updating

a share network subnet with neutron. Specify both a neutron network

and a neutron subnet that belongs to that neutron network.

delete manila share servers -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share server id

get manila share servers -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-id: share server id

extend manila share size -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

size: new size of the share, in GBs.

shrink manila share size -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

size: new size of the share, in GBs.

revert manila share to snapshot -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

snapshot_id: the share snapshot id

platform openstack share status-reset

platform openstack share type-get

platform openstack stack add

platform openstack stack del

platform openstack stack get

platform openstack stack resource-get

reset manila share status -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: share id

-status: the share access status, which is new, error, active

get manila share types -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: share type id

-desc: share type description

add openstack stack -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: stack name

project: parent project id

physical_stack: physical stack

-segmentation_id: segmentation id

delete openstack stack -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: stack id

get stacks -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: stack id

get heat stack resources -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: stack id

-resource: stack resource name

platform openstack stack resource-patch

mark the specified resource in the stack as unhealthy

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name id: stack id

-resource: stack resource name

platform openstack stack update

platform openstack subnet add

platform openstack subnet del

platform openstack subnet get

platform openstack subnet update

platform openstack sys-api extension-get

platform openstack sys-api get

update openstack stack -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: stack id

-name: stack name

-desc: stack description

add openstack subnet -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: subnet name

network: parent network id

-gateway: gateway ip

cidr: subnet cidr

-enable-dhcp: enable dhcp

dns: comma separated subnet dns

delete openstack subnet -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: subnet id

get subnets -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: subnet id

-project: project id

-network: network id

update openstack subnet -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: subnet id

-name: subnet name

-desc: subnet description

get api extensions -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get api versions -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

platform openstack sys compute-agent-get

get compute agents. Use guest agents to access files on the disk,
configure networking, and run other applications and scripts in the
guest while it runs. This hypervisor-specific extension is not currently
enabled for KVM. Use of guest agents is possible only if the underlying
service provider uses the Xen driver.

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform openstack sys compute-host-aggregate-get

platform openstack sys compute-host-get

platform openstack sys compute-host-status

get compute host aggregates -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

get physical hosts -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

set physical host status -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

host: host id

platform openstack sys compute-hypervisor-get

platform openstack sys compute-hypervisor-servers

displays extra statistical information from the machine that hosts the
hypervisor through the API for the hypervisor (XenAPI or KVM/libvirt).

displays extra statistical information from the machine that hosts the
hypervisor through the API for the hypervisor (XenAPI or KVM/libvirt).

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform openstack sys compute-hypervisor-stats

platform openstack sys compute-service-get

platform openstack sys compute-zone-get

platform openstack sys network-agent-get

platform openstack sys network-service-provider get

platform openstack sys orchestrator-service-get

platform openstack sys storage-backend-capabilitie

platform openstack sys storage-backend-storage pool-get

compute hypervisors statistics -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

get compute services -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get compute availability zones -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

get network agents -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get api versions -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

get heat services -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

shows capabilities for a storage back end -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

host: host id

lists all back-end storage pools -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

platform openstack sys storage-host-get

lists all hosts summary info that is not disabled

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform openstack sys storage-service-get

platform openstack sys user-get

platform openstack ultra ping

get storage service. -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

get users -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

ultra ping openstack -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-vip: if true check only the vip

platform openstack ultra ping2

platform openstack ultra ping3

ultra ping openstack instances using an heavy query

ultra ping openstack instances components

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name -vip: if true check only the vip

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name -vip: if true check only the vip

platform openstack version get openstack version -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

platform openstack volume add

platform openstack volume api-extensions

platform openstack volume attach

platform openstack volume attachment-get

add volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

name: volume name

size: volume size in Gb

-type: volume type

-snapshot_id: the snapshot id

volume api extensions -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

attach volume from server -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: volume id

instance: instance id

mountpoint: instance mountpoint. ex. /dev/vda

get volume attachments -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: volume id

-instance: instance id

platform openstack volume backend-get

get all back-end storage pools that are known to the scheduler service

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name -hostname: backend storage pool hostname
-backendname: volume backend name

platform openstack volume bootable-status-update

update volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: volume id

-bootable: bootable status

platform openstack volume- clone volume -O, --orchestrator: openstack
platform reference label

clone -P, --project: openstack current project name name: volume name

volume: volume id

project: project id

-volume_type: the volume type id

platform openstack volume del

platform openstack volume detach

platform openstack volume extend

platform openstack volume get

platform openstack volume group-add

platform openstack volume group-del

platform openstack volume group-get

platform openstack volume group-snapshot-add

platform openstack volume group-snapshot-del

platform openstack volume group-snapshot-get

platform openstack volume group-type-add

platform openstack volume group-type-del

platform openstack volume group-type-get

platform openstack volume group-update

platform openstack volume image-metadata-add

platform openstack volume image-metadata-del

delete volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: volume id

-force: force delete

detach volume from server -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: volume id

extend volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: volume id

size: new volume size

get volumes -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

-id: volume id

-limit: requests a page size of items. Use -1 to list all the volume

-offset: used in conjunction with limit to return a slice of items.
offset

is where to start in the list

add volume group -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

name: volume group name

-availability_zone: volume group availability zone

volume_types: the list of volume types. In an environment with

multiple-storage back ends, the scheduler determines where to send

the volume based on the volume type.

group_type: group type id

delete volume group -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: volume group id

get volume groups -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: volume group id

add volume group snapshot -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

group: volume group id

-name: volume group snapshot name

-desc: volume group snapshot description

delete volume group snapshot -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: volume group snapshot id

get volume group snapshots -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

-id: volume group snapshot id

-group: volume group id

add volume group type -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: volume group type name

-group_specs: volume group type specs

delete volume group type -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: volume group type id

get volume group types -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: volume group id

update volume group -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: volume group id

-name: volume group name

-desc: volume group availability zone

-del: One or more volume UUIDs, separated by commas, that you want

to remove from group

-add: One or more volume UUIDs, separated by commas, that you

want to add to group

add volume image metadata -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: snapshot id

metadata: key:value string metadata

del volume image metadata -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: snapshot id

platform openstack volume manage

platform openstack volume message-get

platform openstack volume metadata-add

platform openstack volume metadata-del

platform openstack volume migrate

platform openstack volume snapshot-add

platform openstack volume snapshot-del

platform openstack volume snapshot-get

platform openstack volume snapshot-revert

platform openstack volume snapshot-status-set

platform openstack volume status-set

platform openstack volume type-get

platform openstack volume type-update

platform openstack volume unmanage

platform openstack volume update

metadata: metadata key

manage volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

source_volume_id: source volume id

name: new volume name

-desc: new volume description

volume_type: volume type id

-bootable: bootable value

-host: source volume host

-cluster: source volume cluster

get volume messages -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: volume message id

add volume metadata -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: snapshot id

metadata: key:value string metadata

del volume metadata -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: snapshot id

metadata: metadata key

migrate volume -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

volume_id: volume id

host: host

-force_host_copy: force_host_copy

-lock_volume: lock_volume

add volume snapshots -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

name: snapshot name

volume: volume id

-desc: snapshot description

-force: indicates whether to snapshot, even if the volume is attached

delete volume snapshot -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: snapshot id

get volume snapshots -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

-id: snapshot id

-volume: volume id

-group_snapshot: group snapshot id

revert volume to snapshot -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

volume: volume id

snapshot: snapshot id

set volume snapshot status -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

id: snapshot id

-status: snapshot status

set volume status -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: volume id

-status: volume id

get volume types -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

-id: volume type id

change volume type -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

id: volume id

volume_type: volume type id

unmanage volume -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

id: volume id

update volume -O, --orchestrator: openstack platform reference label -P,
--project: openstack current project name

id: volume id

-name: volume name

platform redis   (redis management)

platform redis cache-del delete cache item -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

-pattern: keys search pattern [default=*]

platform redis cache-get get cache -O, --orchestrator: redis cluster or
single node reference label -D, --database: redis database number

-port: redis port

-db: redis db [default=0]

-pattern: keys search pattern [default=*]

-cursor: cursor [default=0]

-count: count [default=10]

-value: if True show cache value

platform redis client-list client list of redis instances -O,
--orchestrator: redis cluster or single node reference label -D,
--database: redis database number

-port: redis port

platform redis confs config of redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

platform redis delete delete redis records -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

-pattern: keys search pattern [default=*]

platform redis deletes delete redis keys older than a value in seconds

-O, --orchestrator: redis cluster or single node reference label -D,
--database: redis database number

seconds: min ttl accepted

-port: redis port

-db: redis db [default=0]

-pattern: keys search pattern [default=*]

-cursor: cursor [default=0]

-count: cursor [default=10]

platform redis flush flush redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

platform redis get get redis records by pattern -O, --orchestrator:
redis cluster or single node reference label -D, --database: redis
database number

-port: redis port

-pattern: keys search pattern [default=*]

platform redis info info from redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

platform redis inspect inspect redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

-pattern: keys search pattern [default=*]

platform redis ping ping redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

platform redis scan scan redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

-db: redis db [default=0]

-pattern: keys search pattern [default=*]

-cursor: cursor [default=0]

-count: cursor [default=10]

platform redis sentinel-ping ping redis sentinel instances -O,
--orchestrator: redis cluster or single node reference label -D,
--database: redis database number

-port: redis port

platform redis sentinel status

discover redis sentinel status -O, --orchestrator: redis cluster or
single node reference label -D, --database: redis database number

-port: redis port

platform redis set set redis record -O, --orchestrator: redis cluster or
single node reference label -D, --database: redis database number

-port: redis port

key: record key

value: record value

platform redis size size of redis instances -O, --orchestrator: redis
cluster or single node reference label -D, --database: redis database
number

-port: redis port

platform redis summary summary of redis instances -O, --orchestrator:
redis cluster or single node reference label -D, --database: redis
database number

-port: redis port

platform redis test test redis cluster -O, --orchestrator: redis cluster
or single node reference label -D, --database: redis database number

-port: redis port

platform scheduler schedules   (cmp scheduler schedule management)

platform scheduler schedules add

create schedule reading data from a json file

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id] -order: list sort order
[default=DESC] subsystem: cmp subsystem

--entity: cmp entity class

schedule: schedule config in json file

platform scheduler schedules delete

platform scheduler schedules get

delete schedule by name -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

schedule: schedule name

get schedules -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

-name: schedule name

platform scheduler tasks   (cmp scheduler task management)

platform scheduler tasks definitions

platform scheduler tasks get

platform scheduler tasks log

platform scheduler tasks status

platform scheduler tasks test

platform scheduler tasks test2

platform scheduler tasks trace

list all available tasks you can invoke subsystem: cmp subsystem
--entity: cmp entity class

get task instances -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

-id: task uuid

-objid: task entity objid

-trace: task entity objid

show log for worker instances -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

task: task uuid

-index: index name

-sort: sort field. Ex. date:desc

-pretty: if true show pretty logs

-server: server ip

get task instance status -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

task: task uuid

run test task -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

-number: number of iteration to run

-concurrent: number of concurrent task to run

run test scheduled action -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

get task instance execution trace -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

task: task uuid

platform scheduler tasks tree

display list of related tasks in tree-like format

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

subsystem: cmp subsystem

--entity: cmp entity class

id: task uuid

-v: verbose, if true print task steps as well

platform trilio   (trilio platform)

platform trilio auditlog get auditlog of workload manager -O,
--orchestrator: openstack platform reference label -P, --project:
openstack current project name

-time_in_minutes: time in minutes(default is 24 hrs.)

-time_from: From date time in format MM-DD-YYYY

-time_to: To date time in format MM-DD-YYYY (default is current day)

platform trilio license-add add license -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

license_file: license file name

platform trilio license-check check license -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

platform trilio license-get list license -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

platform trilio protected vm-get

platform trilio restore cancel

platform trilio restore delete

platform trilio restore follow

get protected vm -O, --orchestrator: openstack platform reference label
-P, --project: openstack current project name

cancel the shapshot restore -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

restore: unique identifier of trilio workload snapshot restore

delete the shapshot restore -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

restore: unique identifier of trilio workload snapshot restore

follow the execution of a shapshot restore -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

restore: unique identifier of trilio workload snapshot restore

platform trilio restore-get display the snapshot restore -O,
--orchestrator: openstack platform reference label -P, --project:
openstack current project name

-snapshot: snapshot id

-id: snapshot restore id

platform trilio restore server

restore a server from a snapshot. Project with -P must be specified

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name snapshot: unique identifier of trilio
workload snapshot server: server id

-server_name: server name [default=-restore-<..>] -overwrite: if True
overwrite server

-name: restore name

-desc: restore description

-network: target :

-keep_ip: keep original ip

platform trilio restore volume

restore a volume from a snapshot -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

snapshot: unique identifier of trilio workload snapshot

volume: volume id

-restore_name: restore name

-restore_desc: restore description

platform trilio snapshot-add add a snapshot. Project with -P must be
specified

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name workload: workload id

-name: snapshot name

-desc: snapshot description

-full: snapshot full flag.If True make a full snapshot

platform trilio snapshot cancel

cancel a snapshot that is running. If the snapshot operation is in the
middle of the data transfer of a resource, it waits for the data
transfer operation is complete before terminating the snapshot
operation.

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name snapshot: snapshot id

platform trilio snapshot-del delete a snapshot -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

snapshot: snapshot id

platform trilio snapshot-get display the snapshots of the specified
workload

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

-workload: workload id

-id: snapshot id

-date_from: From date in format 'YYYY-MM-DDTHH:MM:SS' eg
2016-10-10T00:00:00, If don't specify time then it takes 00:00 by
default [default=3 day ago]

platform trilio snapshot mount

platform trilio snapshot mounted

platform trilio snapshot umount

-date_to: To date in format 'YYYY-MM-DDTHH:MM:SS', Specify

HH:MM:SS to get snapshots within same day inclusive/exclusive

results for date_from and date_to [default=today]

mount a snapshot to an instance -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

snapshot: snapshot id

instance: instance id where mount snapshot

list of all mounted snapshots -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

umount a snapshot from an instance -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

snapshot: snapshot id

platform trilio status Return the status ( true or false ) of the Cloud
Wide TrilioVault Job Scheduler

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform trilio storage usage

get workload storage usage -O, --orchestrator: openstack platform
reference label -P, --project: openstack current project name

platform trilio tenant-usage Gives storage used and vms protected by
tenants

platform trilio workload-add add a workload. Project with -P must be
specified

platform trilio workload-del delete the workload. Project with -P must
be specified

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name name: workload name

type_id: workload type id

instances: comme separated list of instances -metadata: metadata

-desc: workload description

-fullbackup_interval: fullbackup interval [default=2] -start_date: start
date. Ex. '06/05/2014'

-end_date: end date. Ex. '07/15/2014'

-start_time: start time. Ex. '2:30 PM' [default='4:00 AM'] -interval:
interval. [default=24hrs]

-snapshots_to_retain: snapshots to retain [default=4] -timezone:
timezone [default=Europe/Rome]

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name workload: workload id

platform trilio workload-get get workload -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

-id: workload id

-verbose: workload verbose info

platform trilio workload reset

platform trilio workload status

Reset the workload. TrilioVault uses storage based snapshots for
calculating backup images of application resources. For cinder volumes,
it uses cinder snapshots and for ceph based nova backends, it uses ceph
snapshots for calculating the backup images.

Depending the state of the workload backup operation, each of these
resources may have one or more snapshots outstanding. Workload-reset
deletes all outstanding snapshots on all resources of the application.
Workload-reset is useful if you want to decommission the

application, but you still want to keep all the backups of the
application. NOTE: It is highly recommended to perform workload-reset
before deleting any application resources from OpenStack.

display workloads status with the last snapshot

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name workload: workload id

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name

platform trilio workload types

platform trilio workload unlock

display workload types -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

unlock the workload -O, --orchestrator: openstack platform reference
label -P, --project: openstack current project name

workload: workload id

platform trilio workload update

update the workload. Project with -P must be specified

-O, --orchestrator: openstack platform reference label -P, --project:
openstack current project name workload: workload id

-name: workload name

-instances: comme separated list of instances -metadata: metadata

-desc: workload description

-fullbackup_interval: fullbackup interval

-start_date: start date. Ex. '06/05/2014'

-end_date: end date. Ex. '07/15/2014'

-start_time: start time. Ex. '2:30 PM'

-interval: interval

-snapshots_to_retain: snapshots to retain

-timezone: timezone

-enabled: enable workloa

platform veeam   (veeam platform management)

platform veeam backup-get get backup -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: veeam platform reference label

-job_id: job uid

-uid: backup uid

-name: backup name pattern (es. \*BCK*)

platform veeam job-get get job -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: veeam platform reference label

-uid: job uid

-name: job name pattern (es. \*BCK*)

platform veeam ping ping veeam -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: veeam platform reference label

platform veeam restorepoint-get

get restorepoint -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: veeam platform reference label

-backup_id: backup uid

-uid: restorepoint uid

-name: restorepoint name pattern (es. \*centos*)

platform veeam version get veeam version -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-O, --orchestrator: veeam platform reference label

platform virsh   (libvirt platform)

platform virsh domain-get get libvirt host domains -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

hostip: host ip

-status: domain status can be: 1 - ACTIVE, 2 - INACTIVE, 4 -

PERSISTENT, 8 - TRANSIENT, 16 - RUNNING, 32 - PAUSED, 64 -

SHUTOFF, 128 - OTHER

-id: domain name

platform virsh domain-ping ping libvirt host domains -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

hostip: host ip

-id: domain name

platform virsh domain-stats get libvirt host domain stats -O,
--orchestrator: openstack platform reference label -P, --project:
openstack current project name

hostip: host ip

-id: domain name

platform virsh domain usage

get libvirt host domain usage date -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

hostip: host ip

-id: domain name

platform virsh hosts get libvirt hosts -O, --orchestrator: openstack
platform reference label -P, --project: openstack current project name

platform virsh servers get libvirt host domains -O, --orchestrator:
openstack platform reference label -P, --project: openstack current
project name

hostip: host ip

-status: domain status can be: 1 - ACTIVE, 2 - INACTIVE, 4 -

PERSISTENT, 8 - TRANSIENT, 16 - RUNNING, 32 - PAUSED, 64 -

SHUTOFF, 128 - OTHER

platform vsphere   (vsphere platform)

platform vsphere cluster get

platform vsphere

datacenter-get

platform vsphere

datacenter-sessions

platform vsphere datastore get

get clusters -O, --orchestrator: vsphere platform reference label -P,
--project: vsphere current project name

-id: cluster id

get datacenters -O, --orchestrator: vsphere platform reference label -P,
--project: vsphere current project name

-id: cluster id

get datacenter sessions -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

get datastores -O, --orchestrator: vsphere platform reference label -P,
--project: vsphere current project name

-id: datastore id

platform vsphere dfw exclusion-add

platform vsphere dfw exclusion-del

add member to distributed firewall exclusion list

delete member from distributed firewall exclusion list

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name member: member id

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name member: member id

platform vsphere dfw exclusion-get

platform vsphere dfw-rule add

platform vsphere dfw-rule get

platform vsphere dfw-rules del

platform vsphere dfw section-add

platform vsphere dfw section-check

platform vsphere dfw section-del

platform vsphere dfw section-get

get distributed firewall exclusion list -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

add distributed firewall rule -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

section: section id

name: rule name

-action: rule action: allow or deny

-direction: rule name

-sources: rule sources. Ex. SecurityGroup:securitygroup

22,Ipv4Address:10.1.1.0/24

-dests: rule sources. Ex. SecurityGroup:securitygroup

22,Ipv4Address:10.1.1.0/24

-services: rule services

-appliedto: rule sources. Ex.

DISTRIBUTED_FIREWALL:DISTRIBUTED_FIREWALL

get distributed firewall rules -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

section: section id

rule: rule id

delete distributed firewall rules -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

section: section id

rules: comma separated list of rules id

add distributed firewall sections -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

name: section name

check distributed firewall sections -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

delete distributed firewall sections -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

section: section id

get distributed firewall sections -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

-id: section id

platform vsphere dfw-status get distributed firewall status -O,
--orchestrator: vsphere platform reference label -P, --project: vsphere
current project name

-section: section id

platform vsphere dlr-get list vsphere dlr -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

id: edge id

platform vsphere dvpg-add add vsphere dvpg -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

name: dvpg name

vlan: dvpg vlan

dvs: dvpg dvs

platform vsphere dvpg-del delete vsphere dvpg -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: dvpg id

platform vsphere dvpg-get get dvpgs -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

-id: dvpg id

platform vsphere dvs-get get dvss -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

-id: dvs id

platform vsphere edge-add add vsphere edge -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

name: edge name

datacenter: datacenter mor-id

cluster: cluster mor-id

datastore: datastore mor-id

uplink_dvpg: uplink dvpg mor-id

uplink_ipaddress: uplink address

uplink_prefix: uplink prefix

pwd: admin user password

dns1: dns name server 1

domain: dns zone

platform vsphere edge appliance-get

platform vsphere edge availability-config

get edge appliances -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

-appliance: appliance id

delete vsphere edge -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

platform vsphere edge-del delete vsphere edge -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: edge id

platform vsphere edge dhcp-config

platform vsphere edge-dns config

platform vsphere edge-fw config

platform vsphere edge-fw rule-add

platform vsphere edge-fw rule-del

platform vsphere edge-fw rule-get

platform vsphere edge-fw rule-update

delete vsphere edge -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

delete vsphere edge -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

get edge firewall config -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

add edge firewall rule -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

name: rule name

-action: rule action. Can be: accept, deny

-direction: rule direction. Can be: in, out

-logged: rule logged

-desc: rule description

-enabled: rule name

-source: rule source. list of comma separated item like: ip:, grp:,
vnic:

-dest: rule destination. list of comma separated item like: ip:, grp:,

vnic:

-app: rule application. list of comma separated item like: app:,

ser:proto+port+source_port

delete edge firewall rule -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

rule: rule id

get edge firewall rule -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

rule: rule id

update edge firewall rule -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

edge: edge id

id: rule id

-name: rule name

-desc: rule description

-act: rule action

-dir: rule direction

-src_add: add rule source

-src_del: remove rule source

-dst_add: add rule destination

-dst_del: remove rule destination

-appl: rule application

-logged: enable rule log

-enabled: enable rule

platform vsphere edge-get get vsphere edges -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: edge id

platform vsphere edge-gslb config

platform vsphere edge ipsec-config

platform vsphere edge-job get

platform vsphere edge l2vpn-get

platform vsphere edge-lb app-profile-add

get edge global load balancer config -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

id: edge id

delete vsphere edge -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

get vsphere edge job -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: job id

get vsphere edge l2 vpn config -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

add edge load balancer application profile -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

name: profile name

template: network traffic template {TCP,UDP,HTTP,HTTPS}

-http_redirect_url: HTTP redirect URL

-persistence: persistence method

-expire: persistence time in seconds [Default=300]

-cookie_name: cookie name

-cookie_mode: cookie mode [Default=insert]

-insert_x_forwarded_for: insert X-Forwarded-for HTTP header

[Default=False]

-ssl_passthrough: enable SSL passthrough [Default=False]

-client_ssl_serv_cert: client service certificate id. Required when
client

ssl=True

-client_ssl_ca_cert: client ca certificate id [Optional]

-client_ssl_cipher: client cipher suite [Default=DEFAULT]

-client_auth: whether peer certificate should be verified

[Default=Ignore]

-server_ssl_serv_cert: server service certificate id

-server_ssl_ca_cert: server ca certificate id. Mandatory if -server_auth

is set to Required

-server_ssl_cipher: server cipher suite [Default=DEFAULT]

-server_auth: whether peer certificate should be verified

[Default=Ignore]

-server_ssl_enabled: enable pool side SSL [Default=False]

platform vsphere edge-lb app-profile-del

platform vsphere edge-lb app-profile-get

platform vsphere edge-lb app-profile-update

delete edge load balancer application profile

get edge load balancer application profiles

update edge load balancer application profile

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name

edge: edge id

id: profile id

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name

edge: edge id

-id: application profile id

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name

edge: edge id

id: profile id

-http_redirect_url: HTTP redirect URL

-persistence: persistence method

-expire: persistence time in seconds [Default=300] -cookie_name: cookie
name

-cookie_mode: cookie mode [Default=insert]

-insert_x_forwarded_for: insert X-Forwarded-for HTTP header
[Default=False]

platform vsphere edge-lb config-get

get edge load balancer config -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

platform vsphere edge-lb config-set

set general edge load balancer parameters

-O, --orchestrator: vsphere platform reference label

-P, --project: vsphere current project name

edge: edge id

-acceleration: force load balancer to use L4 engine which is faster and
more efficient than L7 engine

-logging: enable/disable load balancer logging

-log_level: logging level

platform vsphere edge-lb monitor-add

add edge load balancer monitor -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

name: monitor name

type: monitor type {HTTP,HTTPS,TCP,ICMP,UDP}

-interval: interval in seconds in which a server is to be tested

[Default=5]

-timeout: maximum time in seconds in which a response from the

server must be received [Default=15]

-max_retries: maximum number of times the server is tested before it

is declared down [Default=3]

-method: method to send the health check request to the server

[Default=GET for HTTP/HTTPS monitor type]

platform vsphere edge-lb monitor-del

platform vsphere edge-lb monitor-get

-url: URL to GET or POST [Default="/" for HTTP/HTTPS monitor type]

-expected: expected string [Default="HTTP/1" for HTTP/HTTPS

monitor type]

-send: string to be sent to the backend server after a connection is

established. This option is mandatory when monitor type is UDP.

-receive: string to be received from the backend server for

HTTP/HTTPS protocol. This option is mandatory when monitor type is

UDP.

-extension: advanced monitor configuration.

delete edge load balancer monitor -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

id: monitor id

get edge load balancer monitors -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

-id: monitor id

-name: monitor name

platform vsphere edge-lb monitor-update

update edge load balancer service monitor

-O, --orchestrator: vsphere platform reference label

-P, --project: vsphere current project name

edge: edge id

id: monitor id

-interval: interval in seconds in which a server is to be tested
[Default=5]

-timeout: maximum time in seconds in which a response from the server
must be received [Default=15]

-max_retries: maximum number of times the server is tested before it is
declared down [Default=3]

-method: method to send the health check request to the server
[Default=GET for HTTP/HTTPS monitor type]

-url: URL to GET or POST [Default="/" for HTTP/HTTPS monitor type]
-expected: expected string [Default="HTTP/1" for HTTP/HTTPS monitor
type]

-send: string to be sent to the backend server after a connection is
established. This option is mandatory when monitor type is UDP.
-receive: string to be received from the backend server for HTTP/HTTPS
protocol. This option is mandatory when monitor type is UDP.

platform vsphere edge-lb pool-add

platform vsphere edge-lb pool-del

platform vsphere edge-lb pool-get

platform vsphere edge-lb pool-member-add

add edge load balancer pool -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

name: pool name

algorithm: balancing algorithm {round-robin,ip-hash,leastconn,uri}

-desc: pool description

-transparent: whether client IP addresses are visible to the backend

servers

-monitor: health check monitor id

-ip_ver: ip address version

delete edge load balancer pool -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

id: pool id

get edge load balancer pools -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

-id: pool id

-name: pool name

add member to edge load balancer pool -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

id: pool id

name: member name

-ip_addr: member ip address

-grouping_obj_id: member grouping object id

-port: member port

-monit_port: monitor port

-weight: member weight

-max_conn: maximum number of concurrent connections a member

can handle. Default is 0 which means unlimited

-min_conn: minimum number of concurrent connections a member can

handle. Default is 0 which means unlimited

-cond: Whether the member is enabled or disabled. Default is enabled

platform vsphere edge-lb pool-members-del

remove member from edge load balancer pool

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name edge: edge id

pool: pool id

ids: comma separated list of member ids

platform vsphere edge-lb pool-update

update edge load balancer pool -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

id: pool id

platform vsphere edge-lb rule-add

-algorithm: balancing algorithm {round-robin,ip-hash,leastconn,uri}

-transparent: whether client IP addresses are visible to the backend

servers

add edge load balancer application rule -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

name: rule name

script: rule script. If it starts with "@", read content from a file.
E.g.

acl is_site01 hdr_dom(host) -i test-lb.site01.nivolapiemonte.it \|

use_backend test-pool-1 if is_site01

platform vsphere edge-lb rule-del

delete edge load balancer application rules

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name edge: edge id

id: rule id

platform vsphere edge-lb rule-get

get edge load balancer application rules -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

-id: rule id

platform vsphere edge-lb rule-update

update edge load balancer application rules

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name edge: edge id

id: rule id

-name: rule name

-script: rule script

platform vsphere edge-lb start

platform vsphere edge-lb stats-get

platform vsphere edge-lb stop

platform vsphere edge-lb virt-server-add

enable edge load balancer -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

edge: edge id

get edge load balancer statistics -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

-pool: pool id

disable edge load balancer -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

edge: edge id

add edge load balancer virtual server -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

name: virtual server name

ip_address: ip address that the load balancer is listening on

protocol: virtual server protocol {HTTP,HTTPS}

port: port number

app_profile: application profile id

pool: pool id

-desc: virtual server description

-max_conn: maximum concurrent connections

-max_conn_rate: maximum incoming new connection requests per

second

-acceleration_enabled: use faster L4 load balancer engine rather than

L7 load balancer engine

platform vsphere edge-lb virt-server-add-account desc

Add account in description of nsx virtual server

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name edge: edge id

-id: virtual server id

platform vsphere edge-lb virt-server-del

platform vsphere edge-lb virt-server-disable

platform vsphere edge-lb virt-server-enable

platform vsphere edge-lb virt-server-get

platform vsphere edge-lb virt-server-update

delete edge load balancer virtual server -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

id: virtual server id

disable edge load balancer virtual server -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

id: virtual server id

enable edge load balancer virtual server -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

id: virtual server id

get edge load balancer virtual servers -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

-id: virtual server id

update edge load balancer virtual server -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

edge: edge id

id: virtual server id

-enabled: whether the virtual server is enabled

-ip_address: ip address that the load balancer is listening on

-protocol: virtual server protocol

platform vsphere edge-nat config

platform vsphere edge-nat rule-add

platform vsphere edge-nat rule-del

platform vsphere edge route-default-add

platform vsphere edge route-del-all

platform vsphere edge route-get

platform vsphere edge route-static-add

platform vsphere edge route-static-get

platform vsphere edge-set pwd

platform vsphere edge sslvpn-delete

platform vsphere edge sslvpn-disable

platform vsphere edge sslvpn-enable

platform vsphere edge sslvpn-get

platform vsphere edge sslvpn-install-pkg-add

platform vsphere edge sslvpn-install-pkg-del

-port: port number

-app_profile: application profile id

-pool: pool id

get edge nat config -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

add edge nat rule -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

desc: rule description

action: can be dnat, snat

original_address: original address

translated_address: translated address

-logged: if True enable logging

-enabled: if True enable nat

-original_port: original port

-translated_port: translated port

-protocol: protocol

-vnic: vnic

delete edge nat rule -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

rule: rule id

add edge default route -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

gateway: edge gateway

-mtu: mtu

-vnic: vnic

delete edge static route -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

get edge routing info -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

add edge static route -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

desc: rule description

network: network

next_hop: next_hop address

-mtu: mtu

-vnic: if True enable logging

get edge static routes -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

set vsphere edge admin password -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

pwd: edge admin password

delete edge ssl vpn service -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

disable edge ssl vpn service -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

enable edge ssl vpn service -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

get edge ssl vpn config -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

add edge ssl vpn install pkg -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

name: install package name

gateways: comma separated list of gateway. server:port

delete all the edge ssl vpn install pkg -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

id: edge id

install_pkg: install_pkg id

platform vsphere edge sslvpn-install-pkg-del-all

platform vsphere edge sslvpn-ip-pool-add

platform vsphere edge sslvpn-ip-pool-del

platform vsphere edge sslvpn-ip-pool-del-all

platform vsphere edge sslvpn-private-network-add

delete all the edge ssl vpn install pkg -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

id: edge id

add edge ssl vpn ippool -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

-ip_range: ip range. Default 172.30.0.10-172.30.0.99

-netmask: netmask. Default 255.255.255.0

-gateway: gateway. Default 172.30.0.1

-primary_dns: primary dns. Default 10.103.48.1

-secondary_dns: secondary dns. Default 10.103.48.2

-dns_suffix: dns suffix

-wins_server: wins server

delete all the edge ssl vpn ippool -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

ippool: ippool id

delete all the edge ssl vpn ippool -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

add edge ssl vpn private network -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

network: network cidr

-optimize: send tunnel optimize

platform vsphere edge sslvpn-private-network-del

platform vsphere edge sslvpn-private-network-del all

delete all the edge ssl vpn private network

delete all the edge ssl vpn private network

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name id: edge id

network: network id

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name id: edge id

platform vsphere edge sslvpn-server-add

platform vsphere edge sslvpn-session-delete

platform vsphere edge sslvpn-session-get

platform vsphere edge sslvpn-user-add

platform vsphere edge sslvpn-user-del

platform vsphere edge syslog-add

platform vsphere edge syslog-del

platform vsphere edge syslog-get

platform vsphere edge-vnic add

add edge ssl vpn server config -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

ip: server ip address

port: server port

delete vsphere edge sslvpn session -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

session: edge id

get vsphere edge sslvpn sessions -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

add edge ssl vpn user -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

user_id: user id

password: user password

first_name: first name

last_name: last name

desc: user description

-disable: disable user account

-password_never_expires: password never expires

-change_password_on_next_login: change password on next login

delete all the edge ssl vpn user -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

user: user id

add edge syslog servers -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

servers: rsyslog server ip address comma separated

delete edge syslog servers -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: edge id

get edge syslog config -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: edge id

add edge vnic -O, --orchestrator: vsphere platform reference label -P,
--project: vsphere current project name

id: edge id

index: vnic index

-type: vnic type. Uplink or Internal

portgroup: vnic portgroup id

platform vsphere edge-vnic del

platform vsphere edge-vnic get

platform vsphere edge-vnic update

ip: vnic primary ip

delete edge vnic -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

vnic: vnic index

get edge vinics -O, --orchestrator: vsphere platform reference label -P,
--project: vsphere current project name

-id: edge id

-vnic: vnic id

update edge vnic -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: edge id

vnic: vnic index

-secondary_ip_add: add sub-interface

-secondary_ip_del: remove sub-interface

platform vsphere folder-add add vsphere folder -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

name: folder name

desc: folder description

-datacenter: parent datacenter morid

-folder: parent folder morid

platform vsphere folder-del delete vsphere folder -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: folder id

platform vsphere folder-get get folders -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: folder id

platform vsphere folder update

update vsphere folder -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: folder id

-name: folder name

-desc: folder description

-datacenter: parent datacenter morid

-folder: parent folder morid

platform vsphere host-get get hosts -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

-id: host id

platform vsphere ippool-add add vsphere ippool -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

name: ippool name

startip: start ip

stopip: stop ip

gw: gateway

dns1: dns1

dns2: dns2

-prefix: prefix

-dnssuffix: dns zone

platform vsphere ippool-del delete vsphere ippool -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: ippool id

platform vsphere ippool-get get vsphere ippools -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

-id: ippool id

-range: ippool range

platform vsphere ippool-ip release

platform vsphere ippool-ip usage

platform vsphere ippool-ip use

platform vsphere ippool update

release ippool ip -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: ippool id

ip: ippool ip to use

get all allocated ippool ips -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: ippool id

assign ippool ip -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: ippool id

-ip: ippool ip to use

update vsphere ippool -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: ippool id

-name: ippool name

-startip: start ip

-stopip: stop ip

-gw: gateway

-dns1: dns1

-dns2: dns2

-prefix: prefix

-dnssuffix: dns zone

platform vsphere ipset-add add vsphere ipset -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

name: ipset name

desc: ipset description

cidr: list of ip. Ex. 10.112.201.8-10.112.201.14 or cidr

platform vsphere ipset-del delete vsphere ipset -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: ipset id

platform vsphere ipset-get get ipsets -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: ipset id

-range: ipset range

platform vsphere ipset update

update vsphere ipset -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: ipset id

-name: ipset name

platform vsphere lg-del delete logical switch -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: logical switch id

platform vsphere lg-get get logical switch -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: logical switch id

-dvpg: dvpg id

platform vsphere nsx controller-get

platform vsphere nsx manager-event-get

platform vsphere nsx manager-info

platform vsphere nsx manager-reboot

get vsphere nsx manager controllers -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

get vsphere nsx manager events -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

get vsphere nsx manager info -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

reboot vsphere nsx manager -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

platform vsphere ping ping vsphere -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

platform vsphere respool del

platform vsphere respool get

platform vsphere server add

platform vsphere server console

delete resource pool -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: resource pool id

get resource pools -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

-id: resource pool id

add vsphere server [todo:] -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

name: server name

startip: start ip

stopip: stop ip

gw: gateway

dns1: dns1

dns2: dns2

-prefix: prefix

-dnssuffix: dns zone

get vsphere server console -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

platform vsphere server-del delete vsphere server -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: server id

platform vsphere server device-get

platform vsphere server disable-firewall

platform vsphere server disk-add

platform vsphere server disk-del

get vsphere server devices -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

disable vsphere server firewall -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

pwd: server admin password

add disk to vsphere server -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

server_id: server id

size: disk size

datastore_id: datastore id

delete disk from vsphere server -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

platform vsphere server disk-extend

platform vsphere server disk-get

server_id: server id

disk_object_id: disk object id

extend disk of vsphere server -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

disk_object_id: disk object id

size: disk size in Gb

get disk of vsphere server -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

platform vsphere server-get get servers -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: server id

-name: server name

-names: filter by name like

-template: true list only template

-ipaddress: server ipaddress

-dnsname: server dnsname

-cluster: cluster id

platform vsphere server guest-info

get vsphere server guest info -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

platform vsphere server guest-run-cmd

run vsphere server command using guest tool

-O, --orchestrator: vsphere platform reference label -P, --project:
vsphere current project name id: server id

cmd: command

user: user

pwd: password

-params: command params. Use + as space

platform vsphere server network-destroy-config

platform vsphere server network-setup

platform vsphere server-sg add

platform vsphere server-sg del

platform vsphere server-sg get

platform vsphere server snapshot-add

platform vsphere server snapshot-del

platform vsphere server snapshot-get

platform vsphere server snapshot-revert

setup vsphere server network -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

user: user

pwd: password

ipaddr: ip address

setup vsphere server network -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

user: user

pwd: password

ipaddr: ip address

-prefix: ip address

-macaddr: mac address

gw: network gateway

hostname: hostname

dns: comma separated list of dns

dns_search: dns search

add security to server -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: server id

sgid: security group id

remove security from server -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

sgid: security group id

get vsphere server security groups -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

create vsphere server snapshot -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

name: snapshot name

delete vsphere server snapshot -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

snapshot: snapshot id

get vsphere server snapshot -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

-snapshot: snapshot id

revert vsphere server to snapshot -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: server id

snapshot: snapshot id

platform vsphere server- change vsphere server password -O,
--orchestrator: vsphere platform reference label

ssh-change-pwd -P, --project: vsphere current project name id: server id

user: user

pwd: password

newpwd: new password

platform vsphere server ssh-copy-id

platform vsphere server start

platform vsphere server stop

copy ssh key on server -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: server id

user: user

pwd: password

pubkey: ssh public key to set. Specify file name where key is stored

start vsphere server -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

id: server id

stop vsphere server -O, --orchestrator: vsphere platform reference label
-P, --project: vsphere current project name

id: server id

platform vsphere sg-del delete vsphere securitygroup -O, --orchestrator:
vsphere platform reference label -P, --project: vsphere current project
name

id: securitygroup id

-force: if true force delete

platform vsphere sg-get get securitygroups -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

-id: securitygroup id

platform vsphere sg

member-add

platform vsphere sg

member-del

platform vsphere transport zone-get

add vsphere securitygroup member -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: securitygroup id

member: member to add

delete vsphere securitygroup member -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

id: securitygroup id

member: member to remove

get nsx transport zones -O, --orchestrator: vsphere platform reference
label -P, --project: vsphere current project name

-id: transport zone id

platform vsphere vapp-get get vapps -O, --orchestrator: vsphere platform
reference label -P, --project: vsphere current project name

-id: vapp id

platform vsphere version get vsphere version -O, --orchestrator: vsphere
platform reference label -P, --project: vsphere current project name

platform zabbix   (zabbix platform)

platform zabbix action-add add action -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

name: action name

usrgrp_id: usrgrp id

hostgroup_id: hostgroup id

platform zabbix action-del delete action -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: action id

platform zabbix action-get list actions -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix current project name

-id: action id

-eventsource: eventsource id - 0 = trigger, 2 = auto registration

platform zabbix action update-trigger

update action trigger -O, --orchestrator: zabbix platform reference
label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

action_id: action id

hostgroup_id: hostgroup id

severity: severity (number)

platform zabbix action- update action trigger -O, --orchestrator: zabbix
platform reference label

update-trigger-severity -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or 1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

action_id: action id

severity: severity (number)

platform zabbix alert-get list alerts -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: alert id

-field: sort field

platform zabbix host-add add host -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix current project name

file: data file

platform zabbix host-del delete host -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

platform zabbix host disable

disable host -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

platform zabbix host-enable enable host -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

platform zabbix host-get list hosts -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: host id

-field: sort field

-name: host name

platform zabbix host-get groups

platform zabbix host-get interfaces

platform zabbix host-get templates

platform zabbix host-item add

list groups the host belongs to -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

list interfaces used by the host -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

list templates linked to the host -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: host id

add host item -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix current project name

id: host id

name: key name

desc: item description/comment

agent_type: zabbix type. Can be: 0 - Zabbix agent, 1 - SNMPv1 agent,

2 - Zabbix trapper, 3 - simple check, 4 - SNMPv2 agent, 5 - Zabbix

internal, 6 - SNMPv3 agent, 7 - Zabbix agent (active), 8 - Zabbix

aggregate, 9 - web item, 10 - external check, 11 - database monitor, 12

- IPMI agent, 13 - SSH agent, 14 - TELNET agent, 15 - calculated, 16 -

JMX agent.

platform zabbix host-item get

platform zabbix host trigger-get

platform zabbix hostgroup add

platform zabbix hostgroup del

platform zabbix hostgroup get

platform zabbix hostgroup get-hosts

platform zabbix hostgroup get-templates

platform zabbix hostgroup update

platform zabbix interface del

platform zabbix interface get

platform zabbix interface get-hosts

value_type: zabbix value_type. Can be: 0 - numeric float, 1 - character,

2 - log, 3 - numeric unsigned, 4 - text.

interfaceid: zabbix host interfaceid

key: item key

delay: check interval in seconds

history: number of days to keep item history data

trends: number of days to keep item trends data

list host items -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix current project name

-id: host id

-name: host name

-state: host state

list host triggers -O, --orchestrator: zabbix platform reference label
-P, --project: zabbix current project name

id: host id

add group -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

name: group name

delete group -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

list groups -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: group id

-field: sort field

list hosts that belong to a group -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

list templates that belong to a group -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

update group -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

name: group name

delete interface -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

list interfaces -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: group id

list hosts that use the interface -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

platform zabbix it-service get

id: group id

list it services -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: alert id

-sla: if true pirnt calculated sla

platform zabbix ping ping zabbix -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix current project name

platform zabbix problem get

list problems -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix current project name

-id: action id

platform zabbix proxy-add add proxy -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix current project name

name: proxy hostname

platform zabbix proxy-del delete proxy -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: proxy id

platform zabbix proxy-get list proxys -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: proxy id

-field: sort field

platform zabbix template add

platform zabbix template del

platform zabbix template get

platform zabbix template get-groups

platform zabbix template get-hosts

add template -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix current project name

file: data file

delete template -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: template id

list templates -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: template id

-field: sort field

list groups the template belongs to -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

list hosts linked to the template -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: group id

platform zabbix trigger-add add trigger -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix current project name

desc: trigger description

comment: trigger comment

expression: trigger expression

priority: priority type. Can be: 0 (Default) not classified, 1
information,

2 warning, 3 average, 4 high, 5 disaster

platform zabbix trigger-del delete trigger -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: trigger id

platform zabbix trigger-get list triggers -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: trigger id

-field: sort field

-host: host id filter

platform zabbix user-add add user -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

username: user name

passwd: password

usrgrpid: user group id

email: user email

platform zabbix user-del delete user -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix host group name or id. e.g.
Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: user id

platform zabbix user-get list users -O, --orchestrator: zabbix platform
reference label -P, --project: zabbix current project name

-id: user id

platform zabbix user-update update user -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix host group name or id.
e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

user_id: user id

email: users email - separated by comma

severity: severity - 48 default (32 Disaster + 16 High)

platform zabbix usergroup add

platform zabbix usergroup del

platform zabbix usergroup get

add usergroup -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

usergroupname: usergroup name

hostgroup_id: hostgroup id

delete user group -O, --orchestrator: zabbix platform reference label
-P, --project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

id: user group id

list user groups -O, --orchestrator: zabbix platform reference label -P,
--project: zabbix host group name or id. e.g. Csi.Datacenter.Test or

1234..

-size: list page size [default=20]

-page: list page [default=0]

-order: list sort order [default=DESC]

-id: user group id

-field: sort field

platform zabbix version get zabbix version -O, --orchestrator: zabbix
platform reference label -P, --project: zabbix current project name

res   (resource management)

res containers   (resource container management)

res containers add add resource container -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

file: container config as file

res containers delete delete resource container -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: container uuid

res containers discover discover container id: entity uuid resclass:
entity resclass

res containers discover types

discover container resources id: entity uuid

res containers discovers discover container id: entity uuid

res containers get list resource containers -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: container uuid

-name: container name

-container_type: container type

-objid: container authorization id

-state: container state

-attributes: container attributes

-tags: entity tags

-container_type_name: container type name

res containers ping ping resource container id: entity uuid

res containers pings ping all resource containers

res containers synchronize synchronize container resources id: container
id

resclass: entity resclass

-new: add new physical entities

-died: delete not alive physical entities

-changed: update physical entities

-ext_id: physical entity id

res containers synchronizes synchronize container resources id: entity
uuid

res containers types list resource container types

res containers update update resource container -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: container uuid

file: container config as file

res entities   (entities management)

res entities add add resource entity name: resource entity name -desc:
resource entity description

container: resource container uuid

resclass: resource entity class

-ext_id: resource entity physical id

-parent: resource entity parent uuid

-attribute: resource entity attributes

-tags: resource entity tags

res entities cache-del delete resource entity cache id: resource entity
id

res entities cache-get get resource entity cache id: resource entity id

res entities check check resource entity id: resource entity id

res entities config-get get resource entity config id: resource entity
id

res entities config-set update resource entity config id: resource
entity id

key: config key like config.key

-value: config value

res entities delete delete resource entities ids: comma separated
resource entity ids -force: if true force the delete

-deep: if false delete only resource record and permissions

res entities disable-quotas disable resource quotas and metrics discover

res entities enable-quotas enable resource quotas and metrics discover

id: resource entity id id: resource entity id

res entities errors get the last resource error from a job entity:
resource entity is or name

res entities get list resource entities -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: entity id

-name: entity name

-desc: entity description

-container: container uuid or name

-type: entity type

-objid: entity authorization id

-ext_id: entity physical id

-parent: entity parent

-state: entity state

-attributes: entity attributes

-tags: entity tags

res entities linked get linked resource entities id: resource entity id

res entities metrics get resource entity metrics id: resource entity id

res entities patch patch resource entities ids: comma separated resource
entity ids

res entities state reset resource state id: resource entity id

-state: resource state

res entities tag-add add tag to resource id: resource entity id

tag: tag name

res entities tag-del remove tag from resource id: resource entity id

tag: tag name

res entities tag-get get tags of resource -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource id

res entities tree get resource entity tree entity: resource entity is or
name -parent: if True show tree by parent - child

-link: if True show tree by link relation

res entities types list resource entity types -type: entity type

-subsystem: entity type subsystem

res entities update update resource entity id: resource entity id

-name: resource entity name

-desc: resource entity description

-active: resource entity active

-force: if True force resource metadata update and bypass type

specific update

-ext_id: resource physical id

-attribute: resource entity attributes

res links   (links management)

res links add add resource link name: resource link name

type: resource link type

start_resource: start resource uuid

end_resource: end resource uuid

-attributes: resource link attributes

res links delete delete resource links ids: comma separated resource
link uuids -force: if true force the delete

res links get list resource links -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: link uuid

-name: link name

-resource: start or end resource uuid

-type: link type

-objid: link authorization id

-tags: link tags

res links patch patch resource links ids: comma separated resource link
uuids

res links update update resource link id: resource link uuid

-name: resource link name

-type: resource link type

-start_resource: start resource uuid

-end_resource: end resource uuid

-attributes: resource link attributes

res tags   (tags management)

res tags add add resource tag value: resource tag value

res tags delete delete resource tags ids: comma separated resource tag
uuids -force: if true force the delete

res tags get list resource tags -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: tag uuid

-name: tag name

-resource: resource

-container: container uuid or name

-type: tag type

-objid: tag authorization id

-ext_id: tag physical id

-parent: tag parent

-state: tag state

-attributes: tag attributes

-tags: tag tags

res tags patch patch resource tags ids: comma separated resource tag
uuids

res tags update update resource tag id: resource tag uuid -value:
resource tag value

res-awx   (awx orchestrator)

res-awx job-template-get get job templates -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: job template id

res-awx project-get get projects -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: project id

res-dns   (dns orchestrator)

res-dns record-cname-add create new record CNAME (alias ->
hostname.zone)

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id] -order: list sort order
[default=DESC] name: alias to set

hostname: host name

zone: zone name

-ttl: time to live

res-dns record-cname delete

delete an existing record CNAME -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: record id

res-dns record-cname-get get dns record cnames -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: project id

-name: dns name

-host_name: host name

-parent: zone name

-show_expired: if True show record DELETED

res-dns recorda-add create new record A (ip address -> hostname.zone)

res-dns recorda-delete delete an existing record A (ip address ->
hostname.zone)

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id] -order: list sort order
[default=DESC] ipaddress: ip address

hostname: host name

zone: zone name

-ttl: time to livee

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: record id

res-dns recorda-get get dns recordas -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: project id

-name: dns name

-ip_addr: ip address

-parent: zone name

-show_expired: if True show record DELETED

res-dns zone-get get zones -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: project id

res-dns zone-query fetch a zone record -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: zone id

record: record name

res-dns zone-records-import import record in a zone reading from a file

res-elk   (elk orchestrator)

-size: list page size [default=20] -page: list page [default=0]

-field: list sort field [default=id] -order: list sort order
[default=DESC] id: zone id

filename: file name

res-elk role-add add roles -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

name: role name

indice: indice

space_id: space id

res-elk role-delete delete roles -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource role id

res-elk role-get get roles -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: role id

res-elk role-mapping-add add role_mappings -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

name: role_mapping name

role_name: role name

users_email: users email

realm_name: realm name

res-elk role-mapping-delete delete role_mappings -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource role_mapping id

res-elk role-mapping-get get role_mappings -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: role_mapping id

res-elk space-add add spaces -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

id: space id

name: space name

-description: space description

-color: space color

-initials: space initials

res-elk space-delete delete spaces -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource space id

res-elk space-get get spaces -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: space id

res-grafana   (grafana orchestrator)

res-grafana alert notification-add

res-grafana alert notification-delete

res-grafana alert notification-get

add alert_notifications -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

name: alert_notification name

email: alert_notification email

-desc: alert_notification desc

delete alert_notifications -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource alert_notification id

get alert_notifications -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: alert_notification id

res-grafana folder-add add folders -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

name: folder name

-desc: folder desc

res-grafana folder-delete delete folders -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource folder id

res-grafana folder-get get folders -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: folder id

res-grafana team-add add teams -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container

name: team name

-desc: team desc

res-grafana team-delete delete teams -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: resource team id

res-grafana team-get get teams -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: team id

res-openstack   (openstack orchestrator)

res-openstack domain-get get domains -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: domain id

res-openstack flavor-get get flavors -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: flavor id

res-openstack image-get get images -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: image id

res-openstack network-get get networks -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: network id

res-openstack port-get get ports -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: port id

res-openstack project default-quota-get

get project default quotas -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: project id

res-openstack project-get get projects -size: list page size
[default=20] -page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: project id

res-openstack project member-get

res-openstack project member-set

res-openstack project quota-get

res-openstack project quota-set

get project members -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: project id

set project member TODO -size: list page size [default=20] -page: list
page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: project id

type: quota type

quota: quota name

value: quota value

get project quotas -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: project id

set project quotas -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: project id

type: quota type

quota: quota name

value: quota value

res-openstack router-get get routers -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: router id

res-openstack router-port del

res-openstack security group-del-rule

delete router port -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

id: router id

subnet: subnet id

delete security group rule -size: list page size [default=20] -page:
list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

res-openstack security group-get

res-openstack server actions

res-openstack server console

id: security group id

rule: security group rule id

get security groups -size: list page size [default=20] -page: list page
[default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: security group id

get server actions id: server id

get server console id: server id

res-openstack server-del delete server id: server id

res-openstack server-get get servers -size: list page size [default=20]
-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

-id: server id

-name: instance name

-desc: instance description

-parent: instance parent

-state: instance state

-tags: instance tags

-container: container uuid or name

res-openstack server metadata

get server metadata id: server id

res-openstack server-patch patch server id: server id

res-openstack server-resize get server security groups id: server id
flavor: flavor id

res-openstack server runtime

get server console id: server id

res-openstack server-sg-add add openstack server security group id:
server id sg: security group id

res-openstack server-sg-del delete openstack server security group id:
server id sg: security group id

res-openstack server snapshot-add

res-openstack server snapshot-del

res-openstack server snapshot-get

res-openstack server snapshot-revert

add openstack server snapshot id: server id name: snapshot name

delete openstack server snapshot id: server id snapshot: snapshot id

get openstack server snapshots id: server id

revert openstack server to snapshot id: server id snapshot: snapshot id

res-openstack server-start get server security groups id: server id
res-openstack server-stats get server stats id: server id res-openstack
server-stop stop server id: server id

res-openstack server volume-add

res-openstack server volume-del

add volume to server id: server id volume: volume id

get server security groups id: server id volume: volume id

res-openstack share-add add share -size: list page size [default=20]

-page: list page [default=0]

-field: list sort field [default=id]

-order: list sort order [default=DESC]

container: container id

name: share name

-desc: share description

project: share project id

-tags: comma separated list of tags

share_proto: share protocol. A valid value is NFS, CIFS, GlusterFS,

HDFS, or CephFS

size: the share size, in GBs

share_type: The share type id.

-snapshot_id: The id of the share's base snapshot.

-share_group_id: The id of the share group.

-network: id of the network to use

-subnet: id of the subnet to use

-metadata: One or more metadata key and value pairs as a dictionary

of strings.

-availability_zone: The availability zone.

res-openstack share-del delete share -size: list page size [default=20]

-page: list page [default=0]
