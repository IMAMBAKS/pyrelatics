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

