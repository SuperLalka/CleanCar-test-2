FROM quay.io/minio/minio:RELEASE.2025-02-28T09-55-16Z


COPY ./compose/minio/entrypoint /entrypoint
#RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
