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
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'url'},
                {name: 'alias'},
                {name: 'script'},
                
            {name: 'usesMonitorAttribute'},
            {name: 'monitor'},
            {name: 'monitored'},
            {name: 'locking'},
            ]
        ,
                        columns:[{
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
        },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Name'),
            sortable: true,
            width: 70
        },{
                    id: 'url',
                    dataIndex: 'url',
                    header: _t('URL'),
                    sortable: true,
                    width: 200
                },{
                    id: 'alias',
                    dataIndex: 'alias',
                    header: _t('Alias'),
                    sortable: true,
                    width: 200
                },{
                    id: 'script',
                    dataIndex: 'script',
                    header: _t('Script'),
                    sortable: true,
                    width: 200
                },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            sortable: true,
            width: 65
        },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            sortable: true,
            width: 65
        }]
                    });
                    ZC.TwillScriptPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('TwillScriptPanel', ZC.TwillScriptPanel);
            ZC.registerName('TwillScript', _t('Web Transaction'), _t('Web Transactions'));
            
            })(); 

