"""
Generated by generator/generator.py - 2020-08-31 13:55:49.220121
"""
from aiolyric.objects.location import LyricLocation
from tests.responses.location_fixture import location_fixture_response


def test_location(location_fixtrue_response):
    obj = LyricLocation(location_fixtrue_response)
    assert obj.locationID == location_fixtrue_response["locationID"]
    assert obj.name == location_fixtrue_response["name"]
    assert obj.country == location_fixtrue_response["country"]
    assert obj.zipcode == location_fixtrue_response["zipcode"]
    assert (
        obj.devices[0].displayedOutdoorHumidity
        == location_fixtrue_response["devices"][0]["displayedOutdoorHumidity"]
    )
    assert (
        obj.devices[0].vacationHold
        == location_fixtrue_response["devices"][0]["vacationHold"]
    )
    assert (
        obj.devices[0].currentSchedulePeriod
        == location_fixtrue_response["devices"][0]["currentSchedulePeriod"]
    )
    assert (
        obj.devices[0].scheduleCapabilities
        == location_fixtrue_response["devices"][0]["scheduleCapabilities"]
    )
    assert (
        obj.devices[0].scheduleType
        == location_fixtrue_response["devices"][0]["scheduleType"]
    )
    assert (
        obj.devices[0].scheduleStatus
        == location_fixtrue_response["devices"][0]["scheduleStatus"]
    )
    assert (
        obj.devices[0].allowedTimeIncrements
        == location_fixtrue_response["devices"][0]["allowedTimeIncrements"]
    )
    assert (
        obj.devices[0].settings == location_fixtrue_response["devices"][0]["settings"]
    )
    assert (
        obj.devices[0].deviceClass
        == location_fixtrue_response["devices"][0]["deviceClass"]
    )
    assert (
        obj.devices[0].deviceType
        == location_fixtrue_response["devices"][0]["deviceType"]
    )
    assert (
        obj.devices[0].deviceID == location_fixtrue_response["devices"][0]["deviceID"]
    )
    assert (
        obj.devices[0].userDefinedDeviceName
        == location_fixtrue_response["devices"][0]["userDefinedDeviceName"]
    )
    assert obj.devices[0].name == location_fixtrue_response["devices"][0]["name"]
    assert obj.devices[0].isAlive == location_fixtrue_response["devices"][0]["isAlive"]
    assert (
        obj.devices[0].isUpgrading
        == location_fixtrue_response["devices"][0]["isUpgrading"]
    )
    assert (
        obj.devices[0].isProvisioned
        == location_fixtrue_response["devices"][0]["isProvisioned"]
    )
    assert obj.devices[0].macID == location_fixtrue_response["devices"][0]["macID"]
    assert (
        obj.devices[0].deviceSettings
        == location_fixtrue_response["devices"][0]["deviceSettings"]
    )
    assert obj.devices[0].service == location_fixtrue_response["devices"][0]["service"]
    assert (
        obj.devices[0].deviceRegistrationDate
        == location_fixtrue_response["devices"][0]["deviceRegistrationDate"]
    )
    assert (
        obj.devices[0].dataSyncStatus
        == location_fixtrue_response["devices"][0]["dataSyncStatus"]
    )
    assert obj.devices[0].units == location_fixtrue_response["devices"][0]["units"]
    assert (
        obj.devices[0].indoorTemperature
        == location_fixtrue_response["devices"][0]["indoorTemperature"]
    )
    assert (
        obj.devices[0].outdoorTemperature
        == location_fixtrue_response["devices"][0]["outdoorTemperature"]
    )
    assert (
        obj.devices[0].allowedModes
        == location_fixtrue_response["devices"][0]["allowedModes"]
    )
    assert (
        obj.devices[0].deadband == location_fixtrue_response["devices"][0]["deadband"]
    )
    assert (
        obj.devices[0].hasDualSetpointStatus
        == location_fixtrue_response["devices"][0]["hasDualSetpointStatus"]
    )
    assert (
        obj.devices[0].minHeatSetpoint
        == location_fixtrue_response["devices"][0]["minHeatSetpoint"]
    )
    assert (
        obj.devices[0].maxHeatSetpoint
        == location_fixtrue_response["devices"][0]["maxHeatSetpoint"]
    )
    assert (
        obj.devices[0].minCoolSetpoint
        == location_fixtrue_response["devices"][0]["minCoolSetpoint"]
    )
    assert (
        obj.devices[0].maxCoolSetpoint
        == location_fixtrue_response["devices"][0]["maxCoolSetpoint"]
    )
    assert (
        obj.devices[0].changeableValues
        == location_fixtrue_response["devices"][0]["changeableValues"]
    )
    assert (
        obj.devices[0].operationStatus
        == location_fixtrue_response["devices"][0]["operationStatus"]
    )
    assert (
        obj.devices[0].deviceModel
        == location_fixtrue_response["devices"][0]["deviceModel"]
    )
    assert obj.users[0].userID == location_fixtrue_response["users"][0]["userID"]
    assert obj.users[0].username == location_fixtrue_response["users"][0]["username"]
    assert obj.users[0].firstname == location_fixtrue_response["users"][0]["firstname"]
    assert obj.users[0].lastname == location_fixtrue_response["users"][0]["lastname"]
    assert obj.users[0].created == location_fixtrue_response["users"][0]["created"]
    assert obj.users[0].deleted == location_fixtrue_response["users"][0]["deleted"]
    assert obj.users[0].activated == location_fixtrue_response["users"][0]["activated"]
    assert (
        obj.users[0].connectedHomeAccountExists
        == location_fixtrue_response["users"][0]["connectedHomeAccountExists"]
    )
    assert (
        obj.users[0].locationRoleMapping
        == location_fixtrue_response["users"][0]["locationRoleMapping"]
    )
    assert obj.users[0].isOptOut == location_fixtrue_response["users"][0]["isOptOut"]
    assert (
        obj.users[0].isCurrentUser
        == location_fixtrue_response["users"][0]["isCurrentUser"]
    )
    assert obj.timeZone == location_fixtrue_response["timeZone"]
    assert obj.ianaTimeZone == location_fixtrue_response["ianaTimeZone"]
    assert (
        obj.daylightSavingTimeEnabled
        == location_fixtrue_response["daylightSavingTimeEnabled"]
    )
    assert obj.geoFenceEnabled == location_fixtrue_response["geoFenceEnabled"]
    assert obj.predictiveAIREnabled == location_fixtrue_response["predictiveAIREnabled"]
    assert obj.comfortLevel == location_fixtrue_response["comfortLevel"]
    assert (
        obj.geoFenceNotificationEnabled
        == location_fixtrue_response["geoFenceNotificationEnabled"]
    )
    assert (
        obj.geoFenceNotificationTypeId
        == location_fixtrue_response["geoFenceNotificationTypeId"]
    )
    assert (
        obj.configuration.faceRecognition.enabled
        == location_fixtrue_response["configuration"]["faceRecognition"]["enabled"]
    )
    assert (
        obj.configuration.faceRecognition.maxPersons
        == location_fixtrue_response["configuration"]["faceRecognition"]["maxPersons"]
    )
    assert (
        obj.configuration.faceRecognition.maxEtas
        == location_fixtrue_response["configuration"]["faceRecognition"]["maxEtas"]
    )
    assert (
        obj.configuration.faceRecognition.maxEtaPersons
        == location_fixtrue_response["configuration"]["faceRecognition"][
            "maxEtaPersons"
        ]
    )
    assert (
        obj.configuration.faceRecognition.schedules[0].time
        == location_fixtrue_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["time"]
    )
    assert (
        obj.configuration.faceRecognition.schedules[0].days
        == location_fixtrue_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["days"]
    )
