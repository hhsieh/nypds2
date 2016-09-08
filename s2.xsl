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
      <xsl:apply-templates select="soloists"/>
  </xsl:template>

  <xsl:template match="soloists">
      <xsl:apply-templates select="soloist"/>
  </xsl:template>

  <xsl:template match="soloist">
      <xsl:apply-templates select="soloist"/>
  </xsl:template>


  <xsl:template match="soloist">
    <xsl:copy>
      <programID><xsl:value-of select="ancestor::program/programID"/></programID>
      <season><xsl:value-of select="ancestor::program/season"/></season>
      <composerName><xsl:value-of select="ancestor::program/worksInfo/work/composerName"/></composerName>
      <workTitle><xsl:value-of select="ancestor::program/worksInfo/work/workTitle"/></workTitle>
      <movement><xsl:value-of select="ancestor::program/worksInfo/work/movement"/></movement>
      <conductorName><xsl:value-of select="ancestor::program/worksInfo/work/conductorName"/></conductorName>
      <soloistName><xsl:value-of select="soloistName"/></soloistName>
      <soloistInstrument><xsl:value-of select="soloistInstrument"/></soloistInstrument>
      <soloistRole><xsl:value-of select="soloistRole"/></soloistRole>
    </xsl:copy>
  </xsl:template>

</xsl:transform>


