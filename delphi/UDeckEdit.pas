unit UDeckEdit;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, cxGraphics, cxControls, cxLookAndFeels, cxLookAndFeelPainters,
  cxContainer, cxEdit, dxSkinsCore, dxSkinBlack, dxSkinBlue, dxSkinCaramel,
  dxSkinCoffee, dxSkinDarkRoom, dxSkinDarkSide, dxSkinFoggy, dxSkinGlassOceans,
  dxSkiniMaginary, dxSkinLilian, dxSkinLiquidSky, dxSkinLondonLiquidSky,
  dxSkinMcSkin, dxSkinMoneyTwins, dxSkinOffice2007Black, dxSkinOffice2007Blue,
  dxSkinOffice2007Green, dxSkinOffice2007Pink, dxSkinOffice2007Silver,
  dxSkinOffice2010Black, dxSkinOffice2010Blue, dxSkinOffice2010Silver,
  dxSkinPumpkin, dxSkinSeven, dxSkinSharp, dxSkinSilver, dxSkinSpringTime,
  dxSkinStardust, dxSkinSummer2008, dxSkinsDefaultPainters, dxSkinValentine,
  dxSkinXmas2008Blue, DB, ADODB, cxTextEdit, cxMemo, cxDBEdit, cxImage,
  cxGroupBox, cxStyles, dxSkinscxPCPainter, cxCustomData, cxFilter, cxData,
  cxDataStorage, cxDBData, Menus, StdCtrls, cxButtons, cxLabel,
  cxGridCustomTableView, cxGridTableView, cxGridDBTableView, cxGridLevel,
  cxClasses, cxGridCustomView, cxGrid;

type
  TfrmDeckEdit = class(TForm)
    grpCard: TcxGroupBox;
    imgCard: TcxDBImage;
    memoDesc: TcxDBMemo;
    qryCards: TADOQuery;
    qryCardsid: TAutoIncField;
    qryCardsnome: TStringField;
    qryCardscodigo: TStringField;
    qryCardsdescricao: TMemoField;
    qryCardsnivel: TIntegerField;
    qryCardstipo: TStringField;
    qryCardsatributo: TStringField;
    qryCardsataque: TIntegerField;
    qryCardsdefesa: TIntegerField;
    qryCardscategoria: TStringField;
    qryCardsimage: TBlobField;
    dsCards: TDataSource;
    cxGrid1DBTableView1: TcxGridDBTableView;
    cxGrid1Level1: TcxGridLevel;
    cxGrid1: TcxGrid;
    cxGrid1DBTableView1nome: TcxGridDBColumn;
    cxLabel1: TcxLabel;
    cxLabel2: TcxLabel;
    cxGrid2: TcxGrid;
    cxGridDBTableView1: TcxGridDBTableView;
    cxGridLevel1: TcxGridLevel;
    btnAdicionar: TcxButton;
    btnRemover: TcxButton;
    qryDeck: TADOQuery;
    dsDeck: TDataSource;
    qryDeckid: TAutoIncField;
    qryDecknome: TStringField;
    qryDeckcodigo: TStringField;
    qryDeckdescricao: TMemoField;
    qryDecknivel: TIntegerField;
    qryDecktipo: TStringField;
    qryDeckatributo: TStringField;
    qryDeckataque: TIntegerField;
    qryDeckdefesa: TIntegerField;
    qryDeckcategoria: TStringField;
    qryDeckimage: TBlobField;
    qryDeckqtd: TIntegerField;
    cxGridDBTableView1nome: TcxGridDBColumn;
    cxGridDBTableView1qtd: TcxGridDBColumn;
    lblStatus: TcxLabel;
    lblTipo: TcxLabel;
    cmdSQL: TADOCommand;
    cxLabel3: TcxLabel;
    lblTotal: TcxLabel;
    procedure cxGrid1DBTableView1CellClick(Sender: TcxCustomGridTableView;
      ACellViewInfo: TcxGridTableDataCellViewInfo; AButton: TMouseButton;
      AShift: TShiftState; var AHandled: Boolean);
    procedure cxGridDBTableView1CellClick(Sender: TcxCustomGridTableView;
      ACellViewInfo: TcxGridTableDataCellViewInfo; AButton: TMouseButton;
      AShift: TShiftState; var AHandled: Boolean);
    procedure FormShow(Sender: TObject);
    procedure dsDeckDataChange(Sender: TObject; Field: TField);
    procedure dsCardsDataChange(Sender: TObject; Field: TField);
    procedure btnAdicionarClick(Sender: TObject);
    procedure btnRemoverClick(Sender: TObject);
    procedure qryDeckAfterOpen(DataSet: TDataSet);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmDeckEdit: TfrmDeckEdit;

implementation

uses UDataBase, UMain;

{$R *.dfm}

procedure TfrmDeckEdit.btnAdicionarClick(Sender: TObject);
var
   qrySQL: TADOQuery;
begin
   try
      qrySQL := TADOQuery.Create(self);
      qrySQL.Connection := DTM.Connection;

      qrySQL.SQL.Add('select id, qtd from user_cards where card = :card and user = :user');
      qrySQL.Parameters.ParamByName('card').Value := qryCardsid.AsInteger;
      qrySQL.Parameters.ParamByName('user').Value := frmMain.userID;
      qrySQL.Active := True;

      if qrySQL.Eof then
      begin
         cmdSQL.CommandText := 'insert into user_cards (user, card, qtd) values ' +
         '(:user, :card, :qtd)';
         cmdSQL.Parameters.ParamByName('user').Value := frmMain.userID;
         cmdSQL.Parameters.ParamByName('card').Value := qryCardsid.AsInteger;
         cmdSQL.Parameters.ParamByName('qtd').Value := 1;
         cmdSQL.Execute;

         qryDeck.Close;
         qryDeck.Open;
      end else
      begin
         if qrySQL.Fields[1].AsInteger = 3 then
         begin
            MessageDlg('S� � poss�vel ter 3 c�pias da mesma carta em seu Deck!',
            mtWarning, [mbOK], 0);
            exit;
         end else
         begin
            cmdSQL.CommandText := 'update user_cards set qtd = :qtd where id = :id';
            cmdSQL.Parameters.ParamByName('qtd').Value := qrySQL.Fields[1].AsInteger + 1;
            cmdSQL.Parameters.ParamByName('id').Value := qrySQL.Fields[0].AsInteger;
            cmdSQL.Execute;

            qryDeck.Close;
            qryDeck.Open;
         end;
      end;

   finally
      FreeAndNil(qrySQL);
   end;


  cmdSQL.CommandText := 'select card from user_cards where card = :card and user = :user';
  cmdSQL.Parameters.ParamByName('card').Value := qryCardsid.AsInteger;
  cmdSQL.Parameters.ParamByName('user').Value := frmMain.userID;
  cmdSQL.Execute;

  //cmdSQL.CommandText := 'insert into user_cards(user, card)'
end;

procedure TfrmDeckEdit.btnRemoverClick(Sender: TObject);
var
   pos: TBookmark;
begin
   if qryDeck.RecordCount = 0 then
      exit;

   if qryDeckqtd.AsInteger > 1 then
   begin
      pos := qryDeck.GetBookmark;

      cmdSQL.CommandText := 'update user_cards set qtd = :qtd where card = :card';
      cmdSQL.Parameters.ParamByName('qtd').Value := qryDeckqtd.AsInteger - 1;
      cmdSQL.Parameters.ParamByName('card').Value := qryDeckid.AsInteger;
      cmdSQL.Execute;

      qryDeck.Close;
      qryDeck.Open;
      qryDeck.GotoBookmark(pos);
   end else
   begin
      cmdSQL.CommandText := 'delete from user_cards where card = :card';
      cmdSQL.Parameters.ParamByName('card').Value := qryDeckid.AsInteger;
      cmdSQL.Execute;

      qryDeck.Close;
      qryDeck.Open;
   end;
end;

procedure TfrmDeckEdit.cxGrid1DBTableView1CellClick(Sender: TcxCustomGridTableView;
  ACellViewInfo: TcxGridTableDataCellViewInfo; AButton: TMouseButton;
  AShift: TShiftState; var AHandled: Boolean);
begin
   imgCard.DataBinding.DataSource := dsCards;
   memoDesc.DataBinding.DataSource := dsCards;
end;

procedure TfrmDeckEdit.cxGridDBTableView1CellClick(Sender: TcxCustomGridTableView;
  ACellViewInfo: TcxGridTableDataCellViewInfo; AButton: TMouseButton;
  AShift: TShiftState; var AHandled: Boolean);
begin
   imgCard.DataBinding.DataSource := dsDeck;
   memoDesc.DataBinding.DataSource := dsDeck;
end;

procedure TfrmDeckEdit.dsCardsDataChange(Sender: TObject; Field: TField);
var
  status: String;
begin
  if qryCardscategoria.AsString = 'Monster' then
  begin
    status := 'ATK/' + qryCardsataque.AsString + ' DEF/' + qryCardsdefesa.AsString;
    lblStatus.Caption := status;
    lblTipo.Caption := '[' + qryCardstipo.AsString + ']';

    lblStatus.Visible := True;
    lblTipo.Visible := True;

    memoDesc.Height := 280;
  end else
  begin
    lblStatus.Visible := False;
    lblTipo.Visible := False;

    memoDesc.Height := 310;
  end;

end;

procedure TfrmDeckEdit.dsDeckDataChange(Sender: TObject; Field: TField);
var
  status: String;
begin
  if qryDeckcategoria.AsString = 'Monster' then
  begin
    status := 'ATK/' + qryDeckataque.AsString + ' DEF/' + qryDeckdefesa.AsString;
    lblStatus.Caption := status;
    lblTipo.Caption := '[' + qryDecktipo.AsString + ']';

    lblStatus.Visible := True;
    lblTipo.Visible := True;

    memoDesc.Height := 280;
  end else
  begin
    lblStatus.Visible := False;
    lblTipo.Visible := False;

    memoDesc.Height := 310;
  end;

end;

procedure TfrmDeckEdit.FormShow(Sender: TObject);
begin
   qryDeck.Active := False;
   qryDeck.Parameters.ParamByName('user').Value := frmMain.userID;
   qryDeck.Active := True;

   qryCards.Active := True;
end;

procedure TfrmDeckEdit.qryDeckAfterOpen(DataSet: TDataSet);
var
   TOTAL: Integer;
begin
   qryDeck.First;
   TOTAL := 0;

   while not qryDeck.Eof do
   begin
      TOTAL := TOTAL + qryDeckqtd.AsInteger;
      qryDeck.Next;
   end;

   lblTotal.Caption := IntToStr(TOTAL);

end;

end.
