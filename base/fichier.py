              {% if perms.base.view_systemestockage %}
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:systeme_stockage-list' %}">Voir les systeme de stockages </a></li>
              {%else%}
              <li class="nav-item"> <a class="nav-link" href="#">Voir les systeme de stockages </a></li>
              {%endif%}
              {% if perms.base.add_systemestockage %}
              <li class="nav-item"> <a class="nav-link" href="{% url 'base:create-systeme_stockage' %}">creer une systeme de stockage</a></li>
              {%else%}
              <li class="nav-item"> <a class="nav-link" href="#">creer une systeme de stockage </a></li>
              {%endif%}