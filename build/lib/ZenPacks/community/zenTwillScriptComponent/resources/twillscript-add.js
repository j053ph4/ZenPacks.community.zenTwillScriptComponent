(function() {

/**
* On the device details page the uid is
* Zenoss.env.device_uid and on most other pages it is set with
* the environmental variable PARENT_CONTEXT;
**/
    function getPageContext() {
        return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
    }

    Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
        var menuButton = Ext.getCmp('component-add-menu');
        menuButton.menuItems.push({
			xtype: 'menuitem',
            text: _t('Add Twill Script') + '...',
            hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
            handler: function() {
                var win = new Zenoss.dialog.CloseDialog({
                    width: 300,
                    title: _t('Add Twill Script'),
                    items: [{
                        xtype: 'form',
                        buttonAlign: 'left',
                        monitorValid: true,
                        labelAlign: 'top',
                        footerStyle: 'padding-left: 0',
                        border: false,
                        items: [{
                        	xtype: 'textfield',
                            name: 'name',
                            fieldLabel: _t('Component Name'),
                            id: "nameField",
                            width: 260,
                            allowBlank: false
                        },{
                            xtype: 'textfield',
                            name: 'url',
                            fieldLabel: _t('URL'),
                            id: "urlField",
                            width: 260,
                            allowBlank: true
                        },{
                            xtype: 'textarea',
                            name: 'script',
                            fieldLabel: _t('Script'),
                            id: "scriptField",
                            width: 260,
                            allowBlank: true
                        }],
                        buttons: [{
                            xtype: 'DialogButton',
                            id: 'zenTwillScript-submit',
                            text: _t('Add'),
                            formBind: true,
                            handler: function(b) {
                                var form = b.ownerCt.ownerCt.getForm();
                                var opts = form.getFieldValues();
                                Zenoss.remote.zenTwillScriptRouter.addTwillScriptRouter(opts,
                                function(response) {
                                    if (response.success) {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            title: _t('Script Added'),
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                    else {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                });
                            }
                        }, Zenoss.dialog.CANCEL]
                    }]
                });
                win.show();
            }
        });
    });
}());
