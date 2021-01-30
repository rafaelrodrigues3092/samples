FROM mcr.microsoft.com/mssql/rhel/server:2019-CU8-rhel-8

COPY . /
USER root
RUN chmod +x db-init.sh

RUN /opt/mssql/bin/mssql-conf set sqlagent.enabled true
RUN /opt/mssql/bin/mssql-conf set hadr.hadrenabled  1
RUN /opt/mssql/bin/mssql-conf set memory.memorylimitmb 2048

CMD /bin/bash ./entrypoint.sh
