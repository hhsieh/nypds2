<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output version="1.0" encoding="UTF-8" indent="yes" />
<xsl:strip-space elements="*"/>

  <xsl:template match="program">
    <data>
      <xsl:apply-templates select="worksInfo"/>
    </data>
  </xsl:template>

  <xsl:template match="worksInfo">    
      <xsl:apply-templates select="work"/>    
  </xsl:template>

  <xsl:template match="work">
    <xsl:copy>
      <programID><xsl:value-of select="ancestor::program/programID"/></programID>
      <season><xsl:value-of select="ancestor::program/season"/></season>
      <workID><xsl:value-of select="@workID"/></workID>
      <composerName><xsl:value-of select="composerName"/></composerName>
      <workTitle><xsl:value-of select="workTitle"/></workTitle>
      <movement><xsl:value-of select="movement"/></movement>
      <conductorName><xsl:value-of select="conductorName"/></conductorName>
    </xsl:copy>
  </xsl:template>

</xsl:transform>

