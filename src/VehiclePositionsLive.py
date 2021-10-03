
########################################################
### Ran this for 15 minutes, received no updates ... ###
########################################################

from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

transport = WebsocketsTransport(url='wss://api.entur.io/realtime/v1/vehicles/subscriptions')

client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

query = gql('''
subscription test{
    vehicles(codespaceId: "RUT") {
    line {
      lineRef
      lineName
    }
    lastUpdated
    location {
      latitude
      longitude
    }
    lastUpdatedEpochSecond
    monitored
    operator {
      operatorRef
    }
    serviceJourney {
      serviceJourneyId
    }
    speed
    vehicleId
    expirationEpochSecond
    expiration
    direction
    delay
    codespace {
      codespaceId
    }
    bearing
    mode
  }
}
''')

for result in client.subscribe(query):
    print("Running.")
    print(result)