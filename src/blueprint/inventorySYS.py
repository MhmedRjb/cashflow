from flask import Blueprint,render_template 

inventorySYS_bp=Blueprint('inventorySYS',__name__)
class inventorySYS():
    @inventorySYS_bp.route('/Elfateh/main/Inventory/')
    def inventory():
        return render_template('inventorySYS.html')
    
    @inventorySYS_bp.route('/Elfateh/main/reports/clinets_statistics')
    def clinets_statistics():
        return render_template('inventorySYS.html')
    
    @inventorySYS_bp.route('/Elfateh/main/reports/genral_statistics')
    def genral_statistics():
        return render_template('inventorySYS.html')
