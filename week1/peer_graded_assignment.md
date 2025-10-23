# Jaguar Land Rover (JLR) cyber incident 2025
1. Summary:
    - JLR was breached by HELLCAT Ransomware Group, leaking gigabytes of sensitive information, including propietary documents, source code and employee data. Breach was enabled throught stolen Jira credentials harvested via InfoStealer malware. Shortly after first attack, another HELLCAT member leaked additional 350gb of sensitive data, not included in original leak.
2. Classification:  
    - Source:
        - External
    - Vector:
        - Endpoint, via credential theft
    - Impact:
        - Finacial, due to halted production and therefore lost sales/business. Estimated loss of 1.9bn pounds in eventual total damage.
        - Operational, JLR stopped production of vehicles for about a month, from beginning of September, to beginning of October
3. Response:
    - JLR quickly isolated affected systems, likely preventing more lateral movement from attackers though their network infrastructure
4. Critical reflection:
    - Full scale use of MFA would make it harder for attackers to gain access to system by just credential theft.
    - Isolating systems one from another would make it more difficult for intruders to move lateraly through companys network.

Source: https://www.cyfirma.com/research/investigation-report-on-jaguar-land-rover-cyberattack/