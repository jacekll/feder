**********************
Utworzenie monitoringu
**********************

W przypadku użytkowania oprogramowania powtarzającym się cyklem będzie utworzenie monitoringu, następnie utworzenie spraw wraz z wysłaniem listów. Odczekanie na nadejście odpowiedzi - listów z urzędów. Następnie określany jest kwestionariusz, a następnie jest on przypisywany do spraw, które są gotowe do tego, aby użytkownicy dokonywali ich analizy.

Utworzenie monitoringu należy rozpocząć od weryfikacji kompletności bazy instytucji, która podlegać będą monitoringowi. Należy dokonać oceny informacji dotychczas zgromadzonych w instancji aplikacji. Warto także dokonać weryfikacji jej aktualności, w miarę dostępnych zasobów.

W przypadku braku określonych podmiotów w bazie adresowej instytucji konieczne jest opracowanie bazy adresowej instytucji. Szczegółowe wymagania w tym zakresie zostały przedstawione w :ref:`institutions_database` .

W celu wgrania bazy adresowej instytucji możesz wykorzystać API REST (dostępne pod adresem ``http://example.com/api/institutions/`` , które wspiera metody GET a po uwierzytelnieniu kontem użytkownika PUT, POST i PATCH). Inne formy zmian bazy adresowej systemu pozostają w trakcie opracowania `Eksport instytucji do CSV <https://github.com/watchdogpolska/feder/issues/96>`_ .

W kolejnym kroku przechodzimy do zakładki Szukaj -> Monitoringi -> Dodaj monitoring. Wypełniamy formularz podstawowymi informacjami na jego temat. W tym kroku nie określamy instytucji, które będą adresatami zapytań, ale określamy szablon zapytania, które zostanie do nich przesłane.

.. caution::
   Jeżeli opcja „Dodaj monitoring” jest niedostępna - skontaktuj się z operatorem systemu, aby uzyskać stosowne uprawnienia.

Po przejściu na stosunkowo pustą stronę monitoringu wybieramy przycisk „Przypisz”. Uzyskujesz ekran na którym masz dostępny wykaz instytucji a także możliwość ich odfiltrowania.

Dokonaj starannego wyboru instytucji, które mają być adresatami pytań. Możesz dokonać to przez zaznaczenie każdej z nich indywidualnie. Możesz także umiejętnie operować filtrowaniem, aby uzyskać w zestawieniu tylko podmioty, które mają być adresatami petycji. Pomocne mogą być w tym celu zwłaszcza tagi. Po uzyskaniu takiego zestawienia możesz w 1 wierszu (wierszu nagłówkowym) tabeli zaznaczyć pole, które będzie równoważne oznaczeniu wszystkich podmiotów na wszystkich stronach zestawienia.

Po dokonaniu wyboru instytucji wybierz przycisk „Przypisz (…) i wyślij wniosek”, aby utworzyć sprawy dla każdej z instytucji, a także skierować do niej list.

.. warning::
    Operacja przypisania do sprawy jest nieodwracalna, bowiem automatycznie po przypisaniu do sprawy jest wysyłany wniosek zgodny z szablonem ustalonym dla danego monitoringu.

Po nadejściu odpowiedzi z urzędów będą one automatycznie opublikowane na stronie monitoringu.

.. todo::
    Przedstawić tworzenie kwestionariusza, a następnie formułowania zadań dla niego.
