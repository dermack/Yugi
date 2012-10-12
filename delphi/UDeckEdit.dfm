object frmDeckEdit: TfrmDeckEdit
  Left = 0
  Top = 0
  Caption = 'Edit Deck'
  ClientHeight = 569
  ClientWidth = 898
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object grpCard: TcxGroupBox
    Left = 0
    Top = 0
    Align = alLeft
    TabOrder = 0
    ExplicitHeight = 561
    Height = 569
    Width = 185
    object imgCard: TcxDBImage
      Left = 22
      Top = 24
      AutoSize = True
      DataBinding.DataField = 'image'
      DataBinding.DataSource = dsCards
      TabOrder = 0
      Height = 208
      Width = 140
    end
    object memoDesc: TcxDBMemo
      AlignWithMargins = True
      Left = 6
      Top = 283
      Align = alBottom
      DataBinding.DataField = 'descricao'
      DataBinding.DataSource = dsCards
      Enabled = False
      ParentFont = False
      Properties.Alignment = taCenter
      Style.BorderStyle = ebs3D
      Style.Color = clWindow
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -12
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = []
      Style.Shadow = False
      Style.TextStyle = []
      Style.TransparentBorder = True
      Style.IsFontAssigned = True
      StyleDisabled.TextColor = clBlack
      TabOrder = 1
      ExplicitTop = 275
      Height = 280
      Width = 173
    end
    object lblStatus: TcxLabel
      Left = 32
      Top = 238
      Caption = 'lblStatus'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -12
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
      Visible = False
    end
    object lblTipo: TcxLabel
      Left = 32
      Top = 254
      Caption = 'cxLabel3'
      ParentFont = False
      Style.Font.Charset = DEFAULT_CHARSET
      Style.Font.Color = clWindowText
      Style.Font.Height = -12
      Style.Font.Name = 'Tahoma'
      Style.Font.Style = [fsBold]
      Style.IsFontAssigned = True
      Transparent = True
      Visible = False
    end
  end
  object cxGrid1: TcxGrid
    Left = 638
    Top = 40
    Width = 250
    Height = 505
    TabOrder = 1
    object cxGrid1DBTableView1: TcxGridDBTableView
      NavigatorButtons.ConfirmDelete = False
      OnCellClick = cxGrid1DBTableView1CellClick
      DataController.DataSource = dsCards
      DataController.Summary.DefaultGroupSummaryItems = <>
      DataController.Summary.FooterSummaryItems = <>
      DataController.Summary.SummaryGroups = <>
      OptionsData.Editing = False
      OptionsView.GroupByBox = False
      object cxGrid1DBTableView1nome: TcxGridDBColumn
        Caption = 'Nome'
        DataBinding.FieldName = 'nome'
        Width = 229
      end
    end
    object cxGrid1Level1: TcxGridLevel
      GridView = cxGrid1DBTableView1
    end
  end
  object cxLabel1: TcxLabel
    Left = 651
    Top = 11
    Caption = 'Lista de Cartas Dispon'#237'veis'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -16
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = [fsBold]
    Style.IsFontAssigned = True
    Transparent = True
  end
  object cxLabel2: TcxLabel
    Left = 294
    Top = 11
    Caption = 'Cartas em seu Deck'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -16
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = [fsBold]
    Style.IsFontAssigned = True
    Transparent = True
  end
  object cxGrid2: TcxGrid
    Left = 205
    Top = 40
    Width = 389
    Height = 505
    TabOrder = 4
    object cxGridDBTableView1: TcxGridDBTableView
      NavigatorButtons.ConfirmDelete = False
      OnCellClick = cxGridDBTableView1CellClick
      DataController.DataSource = dsDeck
      DataController.Summary.DefaultGroupSummaryItems = <>
      DataController.Summary.FooterSummaryItems = <>
      DataController.Summary.SummaryGroups = <>
      OptionsData.Editing = False
      OptionsSelection.CellSelect = False
      OptionsView.GroupByBox = False
      object cxGridDBTableView1nome: TcxGridDBColumn
        Caption = 'Nome'
        DataBinding.FieldName = 'nome'
        Width = 304
      end
      object cxGridDBTableView1qtd: TcxGridDBColumn
        Caption = 'Quantidade'
        DataBinding.FieldName = 'qtd'
      end
    end
    object cxGridLevel1: TcxGridLevel
      GridView = cxGridDBTableView1
    end
  end
  object btnAdicionar: TcxButton
    Left = 601
    Top = 175
    Width = 33
    Height = 25
    Caption = '<<'
    TabOrder = 5
    OnClick = btnAdicionarClick
  end
  object btnRemover: TcxButton
    Left = 601
    Top = 206
    Width = 33
    Height = 25
    Caption = '>>'
    TabOrder = 6
    OnClick = btnRemoverClick
  end
  object cxLabel3: TcxLabel
    Left = 205
    Top = 546
    Caption = 'Total de Cartas'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = [fsBold]
    Style.IsFontAssigned = True
    Transparent = True
  end
  object lblTotal: TcxLabel
    Left = 549
    Top = 543
    Caption = '100'
    ParentFont = False
    Style.Font.Charset = DEFAULT_CHARSET
    Style.Font.Color = clWindowText
    Style.Font.Height = -13
    Style.Font.Name = 'Tahoma'
    Style.Font.Style = [fsBold]
    Style.IsFontAssigned = True
    Transparent = True
  end
  object qryCards: TADOQuery
    Connection = DTM.Connection
    CursorType = ctStatic
    Parameters = <>
    SQL.Strings = (
      'select * from cards;')
    Left = 598
    Top = 47
    object qryCardsid: TAutoIncField
      FieldName = 'id'
      ReadOnly = True
    end
    object qryCardsnome: TStringField
      FieldName = 'nome'
      Size = 60
    end
    object qryCardscodigo: TStringField
      FieldName = 'codigo'
      Size = 10
    end
    object qryCardsdescricao: TMemoField
      FieldName = 'descricao'
      BlobType = ftMemo
    end
    object qryCardsnivel: TIntegerField
      FieldName = 'nivel'
    end
    object qryCardstipo: TStringField
      FieldName = 'tipo'
      Size = 45
    end
    object qryCardsatributo: TStringField
      FieldName = 'atributo'
      Size = 10
    end
    object qryCardsataque: TIntegerField
      FieldName = 'ataque'
    end
    object qryCardsdefesa: TIntegerField
      FieldName = 'defesa'
    end
    object qryCardscategoria: TStringField
      FieldName = 'categoria'
      Size = 10
    end
    object qryCardsimage: TBlobField
      FieldName = 'image'
    end
  end
  object dsCards: TDataSource
    DataSet = qryCards
    OnDataChange = dsCardsDataChange
    Left = 599
    Top = 95
  end
  object qryDeck: TADOQuery
    Connection = DTM.Connection
    CursorType = ctStatic
    AfterOpen = qryDeckAfterOpen
    Parameters = <
      item
        Name = 'user'
        Attributes = [paNullable]
        DataType = ftString
        Precision = 255
        Size = 255
        Value = Null
      end>
    SQL.Strings = (
      
        'select cards.*, user_cards.qtd from cards inner join user_cards ' +
        'on'
      'user_cards.card = cards.id where user_cards.user = :user')
    Left = 600
    Top = 287
    object qryDeckid: TAutoIncField
      FieldName = 'id'
      ReadOnly = True
    end
    object qryDecknome: TStringField
      FieldName = 'nome'
      Size = 60
    end
    object qryDeckcodigo: TStringField
      FieldName = 'codigo'
      Size = 10
    end
    object qryDeckdescricao: TMemoField
      FieldName = 'descricao'
      BlobType = ftMemo
    end
    object qryDecknivel: TIntegerField
      FieldName = 'nivel'
    end
    object qryDecktipo: TStringField
      FieldName = 'tipo'
      Size = 45
    end
    object qryDeckatributo: TStringField
      FieldName = 'atributo'
      Size = 10
    end
    object qryDeckataque: TIntegerField
      FieldName = 'ataque'
    end
    object qryDeckdefesa: TIntegerField
      FieldName = 'defesa'
    end
    object qryDeckcategoria: TStringField
      FieldName = 'categoria'
      Size = 10
    end
    object qryDeckimage: TBlobField
      FieldName = 'image'
    end
    object qryDeckqtd: TIntegerField
      FieldName = 'qtd'
    end
  end
  object dsDeck: TDataSource
    DataSet = qryDeck
    OnDataChange = dsDeckDataChange
    Left = 600
    Top = 343
  end
  object cmdSQL: TADOCommand
    Connection = DTM.Connection
    Parameters = <>
    Left = 600
    Top = 432
  end
end
