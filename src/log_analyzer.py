def parse_telemetry(log_list):
    unique_uuids = []
    logic_failures = []

    for log in log_list:
        threat = log.get('threat_details')
        if threat:
            severity = threat.get('severity')
            conf_score = threat.get('confidence_score', 0)
            
            if severity == "CRITICAL":
                uuid = log.get('agent_metadata', {}).get('device_uuid')
                status = log.get('action', {}).get('status')

                if conf_score > 0.95:
                    if status == "SUCCESS":
                        if uuid not in unique_uuids:
                            unique_uuids.append(uuid)
                    else:
                        logic_failures.append(log.get('event_id'))
    return unique_uuids, logic_failures