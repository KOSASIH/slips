# components/slip_list.py
import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemText, Divider } from '@material-ui/core';
import { makeStyles } from '@material-ui/styles';
import SlipCard from './slip_card';

const useStyles = makeStyles((theme) => ({
  list: {
    width: '100%',
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
}));

interface SlipListProps {
  slips: {
    id: number;
    title: string;
    description: string;
    created_at: string;
  }[];
  onDelete: (id: number) => void;
}

const SlipList: React.FC<SlipListProps> = ({ slips, onDelete }) => {
  const classes = useStyles();
  const [filteredSlips, setFilteredSlips] = useState(slips);

  useEffect(() => {
    const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
      const searchTerm = event.target.value.toLowerCase();
      const filteredSlips = slips.filter((slip) => {
        return (
          slip.title.toLowerCase().includes(searchTerm) ||
          slip.description.toLowerCase().includes(searchTerm)
        );
      });
      setFilteredSlips(filteredSlips);
    };

    document.addEventListener('search', handleSearch);

    return () => {
      document.removeEventListener('search', handleSearch);
    };
  }, [slips]);

  return (
    <List className={classes.list}>
      {filteredSlips.map((slip) => (
        <React.Fragment key={slip.id}>
          <ListItem>
            <SlipCard slip={slip} onDelete={onDelete} />
          </ListItem>
          <Divider variant="inset" component="li" />
        </React.Fragment>
      ))}
    </List>
  );
};

export default SlipList;
