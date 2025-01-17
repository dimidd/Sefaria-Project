const {
  LoadingMessage,
  SinglePanelNavHeader,
}                = require('./Misc');
const React      = require('react');
const PropTypes  = require('prop-types');
const classNames = require('classnames');
const Footer     = require('./Footer');
const Sefaria    = require('./sefaria/sefaria');
import Component from 'react-class';

class MyGroupsPanel extends Component {
  componentDidMount() {
    if (!Sefaria.groupsList()) {
      Sefaria.groupsList(function() {
        this.forceUpdate();
      }.bind(this));
    }
  }
  render() {
    var groupsList = Sefaria.groupsList();
    var classes = {myGroupsPanel: 1, systemPanel: 1, readerNavMenu: 1, noHeader: 1 };
    var classStr = classNames(classes);
    return (
      <div className={classStr}>
        {this.props.multiPanel ? null :
          <SinglePanelNavHeader
            enTitle="My Groups"
            heTitle="הקבוצות שלי"
            navHome={this.props.navHome}
            showDisplaySettings={false}/>
        }
        <div className="content hasFooter">
          <div className="contentInner">
            {this.props.multiPanel ?
            <h1>
              <span className="int-en">My Groups</span>
              <span className="int-he">הקבוצות שלי</span>
            </h1> : null }
            {this.props.multiPanel ?
            <center>
              <a className="button white" href="/groups/new">
                <span className="int-en">Create a Group</span>
                <span className="int-he">צור קבוצה</span>
              </a>
            </center> : null }

            <div className="groupsList">
              { groupsList ?
                  (groupsList.private.length ?
                    groupsList.private.map(function(item) {
                      return <GroupListing data={item} key={item.name} />
                    })
                    : <LoadingMessage message="You aren't a member of any groups yet." heMessage="אינך חבר כרגע באף קבוצה" />)
                  : <LoadingMessage />
              }
            </div>

          </div>
          <Footer />
        </div>
      </div>);
  }
}
MyGroupsPanel.propTypes = {};


class PublicGroupsPanel extends Component {
  componentDidMount() {
    if (!Sefaria.groupsList()) {
      Sefaria.groupsList(function() {
        this.forceUpdate();
      }.bind(this));
    }
  }
  render() {
    var groupsList = Sefaria.groupsList();
    var classes = {myGroupsPanel: 1, systemPanel: 1, readerNavMenu: 1, noHeader: 1 };
    var classStr = classNames(classes);
    return (
      <div className={classStr}>
        {this.props.multiPanel ? null :
          <SinglePanelNavHeader
            enTitle="Public Groups"
            navHome={this.props.navHome}
            showDisplaySettings={false}/>
        }
        <div className="content hasFooter">
          <div className="contentInner">
            {this.props.multiPanel ?
            <h1>
              <span className="int-en">Public Groups</span>
              <span className="int-he">קבוצות</span>
            </h1> : null}
            {this.props.multiPanel ?
            <center>
              <a className="button white" href="/groups/new">
                <span className="int-en">Create a Group</span>
                <span className="int-he">צור קבוצה</span>
              </a>
            </center> : null}

            <div className="groupsList">
              { groupsList ?
                  (groupsList.public.length ?
                    groupsList.public.map(function(item) {
                      return <GroupListing data={item} key={item.name} />
                    })
                    : <LoadingMessage message="You aren't a member of any groups yet." heMessage="אינך חבר כרגע באף קבוצה" />)
                  : <LoadingMessage />
              }
            </div>

          </div>
          <Footer />
        </div>
      </div>);
  }
}
PublicGroupsPanel.propTypes = {};

class GroupListing extends Component {
  render() {
    var imageUrl = this.props.data.imageUrl || "/static/img/group.svg"
    var imageClass = classNames({groupListingImage: 1, default: !this.props.data.imageUrl});
    var groupUrl = "/groups/" + this.props.data.name.replace(/\s/g, "-")
    return (<div className="groupListing">
              <div className="left-content">
                <a href={groupUrl}>
                  <div className="groupListingImageBox">
                    <img className={imageClass} src={imageUrl} alt="Group Logo"/>
                  </div>
                </a>
                <div className="groupListingText">
                  <a href={groupUrl} className="groupListingName">{this.props.data.name}</a>
                  <div className="groupListingDetails">
                    <span className="groupListingDetail groupListingMemberCount">
                      <span className="int-en">{this.props.data.memberCount} Members</span>
                      <span className="int-he">{this.props.data.memberCount} חברים</span>
                    </span>
                    <span className="groupListingDetailSeparator">•</span>
                    <span className="groupListingDetail groupListingSheetCount">
                      <span className="int-en">{this.props.data.sheetCount} Sheets</span>
                      <span className="int-he">{this.props.data.sheetCount} דפים</span>
                    </span>
                  </div>
                </div>
              </div>
              <div className="right-content">
                { this.props.showMembership ? this.props.data.membership : null }
              </div>
            </div>);
  }
}
GroupListing.propTypes = {
  data: PropTypes.object.isRequired,
  showMembership: PropTypes.bool,
};

module.exports.GroupListing = GroupListing;
module.exports.MyGroupsPanel = MyGroupsPanel;
module.exports.PublicGroupsPanel = PublicGroupsPanel;
