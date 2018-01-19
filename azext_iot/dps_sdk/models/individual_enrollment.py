# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IndividualEnrollment(Model):
    """The device enrollment record.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param registration_id: Registration ID.
    :type registration_id: str
    :param device_id: Desired IoT Hub device ID (optional).
    :type device_id: str
    :param registration_state: Current registration status.
    :type registration_state:
     ~microsoft.azure.management.provisioningservices.models.DeviceRegistrationState
    :param attestation: Attestation method used by the device.
    :type attestation:
     ~microsoft.azure.management.provisioningservices.models.AttestationMechanism
    :param iot_hub_host_name: The Iot Hub host name.
    :type iot_hub_host_name: str
    :param initial_twin: Initial device twin.
    :type initial_twin:
     ~microsoft.azure.management.provisioningservices.models.InitialTwin
    :param etag: The entity tag associated with the resource.
    :type etag: str
    :param provisioning_status: The provisioning status. Possible values
     include: 'enabled', 'disabled'
    :type provisioning_status: str or
     ~microsoft.azure.management.provisioningservices.models.enum
    :ivar created_date_time_utc: The DateTime this resource was created.
    :vartype created_date_time_utc: datetime
    :ivar last_updated_date_time_utc: The DateTime this resource was last
     updated.
    :vartype last_updated_date_time_utc: datetime
    """

    _validation = {
        'registration_id': {'required': True},
        'attestation': {'required': True},
        'created_date_time_utc': {'readonly': True},
        'last_updated_date_time_utc': {'readonly': True},
    }

    _attribute_map = {
        'registration_id': {'key': 'registrationId', 'type': 'str'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'registration_state': {'key': 'registrationState', 'type': 'DeviceRegistrationState'},
        'attestation': {'key': 'attestation', 'type': 'AttestationMechanism'},
        'iot_hub_host_name': {'key': 'iotHubHostName', 'type': 'str'},
        'initial_twin': {'key': 'initialTwin', 'type': 'InitialTwin'},
        'etag': {'key': 'etag', 'type': 'str'},
        'provisioning_status': {'key': 'provisioningStatus', 'type': 'str'},
        'created_date_time_utc': {'key': 'createdDateTimeUtc', 'type': 'iso-8601'},
        'last_updated_date_time_utc': {'key': 'lastUpdatedDateTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, registration_id, attestation, device_id=None, registration_state=None, iot_hub_host_name=None, initial_twin=None, etag=None, provisioning_status=None):
        super(IndividualEnrollment, self).__init__()
        self.registration_id = registration_id
        self.device_id = device_id
        self.registration_state = registration_state
        self.attestation = attestation
        self.iot_hub_host_name = iot_hub_host_name
        self.initial_twin = initial_twin
        self.etag = etag
        self.provisioning_status = provisioning_status
        self.created_date_time_utc = None
        self.last_updated_date_time_utc = None