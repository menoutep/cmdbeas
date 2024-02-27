             <div class="row">

              <div class="col-lg-9">
                <h4 class="card-title"> {{network_interface.name}}</h4>
                <p class="card-description">
                  Consulter les détails sur le serveur : {{network_interface.name}}
                </p>
              </div>
              <div class="col-lg-3">
                
                  <div class="dropdown">
                    <button class="btn btn-danger btn-sm dropdown-toggle" type="button" id="dropdownMenuSizeButton3" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                     Action
                    </button>
                    <div class="dropdown-menu show" aria-labelledby="dropdownMenuButton3">
                      <h6 class="dropdown-header">Choisir une action</h6>
                      <a class="dropdown-item" href="{% url 'base:update-network_interface' network_interface.pk %}">Modifier le serveur</a>
                      <div class="dropdown-divider"></div>
                      
                      <a class="dropdown-item" href="{% url 'base:delete-network_interface' network_interface.pk %}">Supprimer le serveur</a>
                      
                    </div>
                  
                </div>
               
              </div>
            </div>