class ServerAdmin(SimpleHistoryAdmin):
    list_filter = ('type_server', 'rack_server_room_datacenter','rack_server_room_datacenter', 'updated')
    history_list_display = ["file"]
    search_fields = ['name', 'file','applications__name']
    empty_value_display = "unknown"
    form = ServerUpdateForm
admin.site.register(Server, ServerAdmin)


     <nav class="sidebar sidebar-offcanvas" id="sidebar">
      <ul class="nav">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'base:index' %}">
            <i class="mdi mdi-grid-large menu-icon"></i>
            <span class="menu-title">Dashboard</span>
          </a>
        </li>
        <li class="nav-item nav-category">Api Documentation Administartion</li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false" aria-controls="ui-basic">
            <i class="menu-icon mdi mdi-floor-plan"></i>
            <span class="menu-title">Documentation api</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="ui-basic">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:api_documentation-list' %}">Voir les documentations </a></li>
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:create-api_documentation' %}">creer une documentation</a></li>
    
            </ul>
          </div>
        </li>

        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#charts" aria-expanded="false" aria-controls="charts">
            <i class="menu-icon mdi mdi-floor-plan"></i>
            <span class="menu-title">Api Specification</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="charts">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:api_specification-list' %}">Voir les spécifications</a></li>
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:create-api_specification' %}">ajouter une spécification</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item nav-category">Datamodel administration</li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#pages" aria-expanded="false"
            aria-controls="pages">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Modèle de données</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="pages">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:data_model-list' %}">Voir modèle de données</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-data_model' %}">Creer un modèle de données</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#rack" aria-expanded="false"
            aria-controls="rack">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Dictionnaires de données</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="rack">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:data_dictionnary-list' %}">Voir dictionnaires de données</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-data_dictionnary' %}">Creer un dictionnaire de données</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#server-room" aria-expanded="false"
            aria-controls="server-room">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">mapping data</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="server-room">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:data_dictionnary_model-list' %}">Voir nos mapping<</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-data_dictionnary_model' %}">Creer un mapping</a></li>
            </ul>
          </div>
        </li>
        
        <li class="nav-item nav-category">Plan reprise désastre</li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#icons" aria-expanded="false"
            aria-controls="icons">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Plan de reprise technique</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="icons">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:technical_recovery_plan-list' %}">Voir nos plan </a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-technical_recovery_plan' %}">Creer un plan</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#form-elements" aria-expanded="false"
            aria-controls="form-elements">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Backup strategie</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="form-elements">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:backupstrategie-list' %}">Voir nos backups strategies</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:backupstrategie-create' %}">Creer une backup strategie</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item nav-category">Architecture et call flow</li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#auth" aria-expanded="false"
            aria-controls="auth">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Diagrammes d'architecture</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="auth">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:architecture_diagram-list' %}">Voir nos diagrammes</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-architecture_diagram' %}">Creer un Serveur diagramme</a></li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="collapse" href="#test" aria-expanded="false"
            aria-controls="test">
            <i class="menu-icon mdi mdi-card-text-outline"></i>
            <span class="menu-title">Call flow</span>
            <i class="menu-arrow"></i>
          </a>
          <div class="collapse" id="test">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item"><a class="nav-link" href="{% url 'base:call_flow-list' %}">Voir nos call flow</a></li>
              <li class="nav-item"><a class="nav-link" href="{% url 'base:create-call_flow' %}">Creer un call flow</a></li>
            </ul>
          </div>
        </li>
       
      </ul>
    </nav>