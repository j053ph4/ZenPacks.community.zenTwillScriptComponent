
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.TwillScriptPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'TwillScript',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "alias"
                    }, 
                    {
                        "name": "script"
                    }, 
                    {
                        "name": "url"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "header": "Alias", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "alias", 
                        "dataIndex": "alias"
                    }, 
                    {
                        "header": "Script", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "script", 
                        "dataIndex": "script"
                    }, 
                    {
                        "header": "URL", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "url", 
                        "dataIndex": "url"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.TwillScriptPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('TwillScriptPanel', ZC.TwillScriptPanel);
    ZC.registerName('TwillScript', _t('Web Transaction'), _t('Web Transactions'));
    
    })();

