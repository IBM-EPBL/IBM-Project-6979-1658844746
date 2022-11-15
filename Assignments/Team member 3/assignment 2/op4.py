@app.route('/api/users/remove_group/<int:groupId>',methods=['DELETE'])
def removeGroup(groupId):
try:
    print 'its working--Delete group'
    if userGroup.query.filter_by(group_id=groupId).first() is not None:
        userGroup.query.filter_by(group_id=groupId).delete()
        message='Group removed succesfully\n'
    else:
        print 'Group not found'
        message='Group not found\n'
except HTTPException as error:
    return error(os.version)
return message
