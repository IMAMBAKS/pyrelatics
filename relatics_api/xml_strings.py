import_xml = """
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <Import xmlns="http://www.relatics.com/">
                <Operation>{Operation}</Operation>
                <Identification>
                    <Identification>
                        <Workspace>{Workspace}</Workspace>
                    </Identification>
                </Identification>
                <Authentication>
                    <Authentication>
                        <Entrycode>{Entrycode}</Entrycode>
                    </Authentication>
                </Authentication>
                <Filename>import_data.xml</Filename>
                <Data>
                    {Data}
                </Data>
            </Import>
        </soap:Body>
    </soap:Envelope>
"""

retrieve_xml = """
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetResult xmlns="http://www.relatics.com/">
                <Operation>{Operation}</Operation>
                <Identification>
                    <Identification>
                        <Workspace>{Workspace}</Workspace>
                    </Identification>
                </Identification>
                <Authentication>
                    <Authentication>
                        <Entrycode>{Entrycode}</Entrycode>
                    </Authentication>
                </Authentication>
            </GetResult>
        </soap:Body>
    </soap:Envelope>
"""

retrieve_token = """
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                       xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <SOAP-ENV:Header>
            <m:Credentials xmlns:m="http://www.relatics.com/">
                <m:Username>{Username}</m:Username>
                <m:Password>{Password}</m:Password>
            </m:Credentials>
        </SOAP-ENV:Header>
        <SOAP-ENV:Body>
            <m:Login xmlns:m="http://www.relatics.com/"/>
        </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
"""

