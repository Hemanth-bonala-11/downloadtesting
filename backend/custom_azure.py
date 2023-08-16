from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    storage_account_key = "FrdtU1SmWi5e7CVJMib2rYNw++T23Z6qjs/qhoyns0UNm6WR7wBFvo94EPwQ6g8gauBwT10HQhUP+AStxXo8Zw=="
    storage_account_name = "oneapidriverlessml"
    connection_string = "DefaultEndpointsProtocol=https;AccountName=oneapidriverlessml;AccountKey=FrdtU1SmWi5e7CVJMib2rYNw++T23Z6qjs/qhoyns0UNm6WR7wBFvo94EPwQ6g8gauBwT10HQhUP+AStxXo8Zw==;EndpointSuffix=core.windows.net"
    container_name = "oneapi"
    account_name = storage_account_name # Must be replaced by your <storage_account_name>
    account_key = storage_account_key # Must be replaced by your <storage_account_key>
    azure_container = container_name
    expiration_secs = None