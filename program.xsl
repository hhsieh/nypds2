<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output version="1.0" encoding="UTF-8" indent="yes" />
<xsl:strip-space elements="*"/>

  <xsl:template match="/">
    <program>
      <xsl:apply-templates select="program"/>
    </program>
  </xsl:template>

  <xsl:template match="program">
    <id><xsl:value-of select="id"/></id>
    <programID><xsl:value-of select="programID"/></programID>
    <orchestra><xsl:value-of select="orchestra"/></orchestra>
    <season><xsl:value-of select="season"/></season>
    <concertInfo><xsl:value-of select="concat(concertInfo/eventType, ' ',
                   concertInfo/Location, ' ', concertInfo/Venue, ' ', 
                   concertInfo/Date, ' ', concertInfo/Time)"/></concertInfo>
  </xsl:template>

</xsl:transform>
